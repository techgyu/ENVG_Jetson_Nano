#include <stdlib.h> // 표준 라이브러리 포함
#include <iostream> // 입출력 스트림 사용
#include <signal.h> // 시그널 처리용 헤더
#include <string> // 문자열 사용
#include <chrono> // 시간 측정용 라이브러리
#include <thread> // 스레드 사용

#include "Lepton3.hpp" // Lepton3 카메라 제어 헤더

/*C++용 opencv2 라이브러리*/
#include <opencv2/core/core.hpp> // OpenCV 핵심 기능, 행렬, 벡터, 기본 연산 등 OpenCV의 핵심 자료 구조와 함수 제공
#include <opencv2/imgproc/imgproc.hpp> // 이미지 필터링, 변환, 윤곽선 검출 등 이미지 처리 함수 제공
#include <opencv2/highgui/highgui.hpp> // 이미지를 화면에 띄우거나, 키보드 입력을 받는 등 GUI 관련 함수 제공

#include "stopwatch.hpp" // 스톱워치(시간 측정) 헤더

using namespace std; // 표준 라이브러리의 모든 이름(함수, 클래스 등)을 별도의 접두사 없이 바로 사용할 수 있게 해주는 선언
// 예를 들어, std::cout 대신 cout로 바로 사용 가능

// ----> Global variables: 전역 변수(프로그램 전체에서 접근하여 사용할 수 있도록 정의)
Lepton3* lepton3=nullptr; // Lepton3 객체 포인터, 카메라를 제어하는 객체의 포인터, 프레임 획득, 모드 변경 등은 해당 포인터를 통해 이뤄짐
    // 상기 객체는 main() 함수에서 객체로서 생성됨(new Lepton3(...))
    // lepton3 -> start(), lepton3 -> getLastFrame16() 등 다양한 맴버 함수를 호출할 때 사용
    // nullptr로 초기화하여 아직 객체가 생성되지 않았음을 명시

static bool close = false; // 종료 플래그
    // 프로그램의 메인 루프가 계속 실행될 지, 종료될 지를 결정하는 플래그
    // false일 때는 루프가 계속 돌고, true가 되면 루프가 종료되어 프로그램이 끝남
    // 예를 들어, 사용자가 'q'키를 누르거나 Ctrl+C 시그널이 들어오면 true로 설정되고, 그 즉시 루프가 종료됨
    // static으로 선언하여, 파일 내에서만 접근 가능하며, 여러 함수에서 값을 변경할 수 있음

static bool rgb_mode = true; // RGB 모드 여부
    // 현재 카메라의 데이터 출력 모드가 RGB 컬러 모드인지, Radiometry(온도값) 모드인지를 나타내는 플래그
    // true일 때는 RGB 컬러 이미지(3채널, 사람이 보기 좋은 컬러맵), false면 Radiometry 모드(16비트 온도 값, 흑백)
    // 키보드에서 c를 누르면 true, r을 누르면 false로 변경됨
    // 이 값은 set_rgb_mode() 함수에서 실제 카메라 설정과 동기화됨.
// <---- Global variables: 전역 변수

// ----> Global functions: 전역 함수(프로그램 전체에서 접근하여 사용할 수 있도록 정의)
void close_handler(int s); // 종료 시그널 처리하는 함수(핸들러)
void keyboard_handler(int key); // 키보드 입력 처리하는 함수(핸들러)
void set_rgb_mode(bool enable); // RGB 모드 설정 함수
// <---- Global functions: 전역 함수



int main (int argc, char *argv[]) // 메인 함수
{
    cout << "OpenCV demo for Lepton3 on Nvidia Jetson" << std::endl; // 시작 메시지 출력
    printf("Code 1\n");
    // ----> Set Ctrl+C handler
    /*구조체란: 여러 개의 변수(데이터)를 하나로 묶어서 새로운 자료형을 만드는 방법*/
    /*파이썬의 딕셔너리와 비슷하게 여러 값을 한 번에 담을 수 있지만*/
    /*키-값 쌍이 아니라 "정해진 맴버 변수"를 가짐*/

    /*sigaction 구조체란: 리눅스/유닉스에서 시그널이 발생했을 때 어떤 동작을 할 지 지정하는 구조체*/
    //sa_handler: 시그널이 발생했을 때 실행할 함수(핸들러) 지정
    //sa_mask: 시그널 처리 중 임시리로 블록할 시그널 집합
    //sa_flags: 추가 옵션(플래그)

    struct sigaction sigIntHandler; // 시그널 핸들러 구조체 선언
    sigIntHandler.sa_handler = close_handler; // 핸들러 함수 지정: 시그널이 발생하면 close_handler() 함수를 실행함
    sigemptyset(&sigIntHandler.sa_mask); // 시그널 마스크 초기화, 시그널 처리 중에 추가로 무시할 시그널이 없도록 초기화
    sigIntHandler.sa_flags = 0; // 플래그 초기화, 특별 옵션 없이 기본 동작만 하도록 설정
    sigaction(SIGINT, &sigIntHandler, NULL); // 시그널 핸들러 등록, 위에서 지정한 옵션으로 동작하도록 시스템에 등록함
    // SIGINT(CTRL + C)가 들어오면 위의 시그널 핸들러(종료 시그널 처리 함수)를 호출하여 처리함
    // 마지막에 들어가 있는 NULL은 이전 핸들러를 저장하지 않음을 의미
    // <---- Set Ctrl+C handler
    printf("Code 2\n");
    Lepton3::DebugLvl deb_lvl = Lepton3::DBG_FULL; // 디버그 레벨 설정
    // Lepton3 카메라 라이브러리에서 제공하는 디버그 레벨(enum)타입 중 "아무 메세지도 출력하지 않는" 모드로 설정
    // 만약 DBG_NONE 대신 DBG_INFO나 DBG_FULL로 설정하면, 카메라와 통신하면서 발생하는 다양한 정보성 메시지들이 출력됨
    printf("Code 3\n");
    /* 실제로 Lepton 3 카메라를 제어할 객체를 동적으로 생성 */
    lepton3 = new Lepton3( "/dev/spidev0.0", "/dev/i2c-0", deb_lvl ); // Lepton3 객체 생성 (SPI, I2C 포트 지정)
    // "/dev/spidev0.0": SPI 장치 파일 경로, "/dev/i2c-0": I2C 장치 파일 경로
    printf("Code 4\n");
    /* 카메라 통신 시작 */
    lepton3->start(); // 카메라 시작
    // 내부적으로 SPI/I2C 장치를 열고, 초기화 과정을 거쳐 데이터 수신 준비를 함
    // 이 함수가 호출되어야 이후에 프레임을 정상적으로 읽을 수 있음
    printf("Code 5\n");
    // Set initial data mode
    set_rgb_mode(rgb_mode); // 초기 RGB 모드 설정
    // 현재 rgb_mode 전역 변수의 값(true)이 전달되어, RGB 모드로 카메라가 설정됨
    // 설정할 수 있는 모드에는 RGB 모드(true)와 Radiometry 모드(false)가 있음
    printf("Code 6\n");
    uint64_t frameIdx=0; // 프레임 인덱스: 현재까지 처리한 프레임(이미지) 개수를 세는 변수, 루프가 돌 떄마다 1씩 증가
    uint16_t min; // 최소값: 카메라에서 받아온 이미지의 최소 픽셀 값
    uint16_t max; // 최대값: 카메라에서 받아온 이미지의 최대 픽셀 값
    // Radiometry(온도값) 모드에서만 의미가 있으며, RGB 모드에서는 사용하지 않음
    uint8_t w,h; // 이미지 폭, 높이
    // 현재 프레임(이미지)의 가로(w)와 세로(h) 크기를 저장하는 변수
    // 카메라에서 프레임을 읽어올 때, 실제 이미지의 해상도를 이 변수에 저장해서 이후 이미지 처리에 사용함.
    // 만약 카메라가 160X120 해상도라면, w=160, h=120이 됨(실제 카메라의 해상도에 따라 값이 달라짐)
    printf("Code 7\n");
    /*프레임 처리 속도(프레임 간 시간 간격, FPS 등)을 측정하기 위한 스톱워치(타이머 기능)*/
    StopWatch stpWtc; // 스톱워치 객체
    printf("Code 8\n");
    stpWtc.tic(); // 시간 측정 시작, stpWtc.toc()를 호출하면 tic()를 호출한 시점부터 얼마나 시간이 흘렀는지(마이크로초 단위 등)으로 알려줌
    printf("Code 9\n");
    while(!close) // 종료 플래그가 false일 때 반복
    {
        printf("Code 10\n");
        const uint16_t* data16 = lepton3->getLastFrame16( w, h, &min, &max ); // 16비트 프레임 데이터 가져오기
        printf("w: %d, h: %d, min: %u, max: %u\n", w, h, min, max);
        printf("frameIdx: %llu\n", frameIdx);
        printf("rgb_mode: %d\n", rgb_mode); 
        if (data16 == nullptr) {
            printf("data16 is NULL\n");
        } else {
            printf("data16: %p\n", data16);
        }
        // Lepton 카메라에서 Radiometry(16비트 온도값) 모드로 촬영한 프레임 데이터를 가져옴, 만약에 없으면 nullptr 반환
        printf("Code 11\n");
        const uint8_t* dataRGB = lepton3->getLastFrameRGB( w, h ); // RGB 프레임 데이터 가져오기
        printf("w: %d, h: %d, min: %u, max: %u\n", w, h, min, max);
        printf("frameIdx: %llu\n", frameIdx);
        printf("rgb_mode: %d\n", rgb_mode);         
        if (dataRGB == nullptr) {
            printf("dataRGB is NULL\n");
        } else {
            printf("dataRGB: %p\n", dataRGB);
        }
        // Lepton 카메라에서 RGB(3채널 컬러맵) 모드로 촬영한 프레임 데이터를 가져옴, 만약에 없으면 nullptr 반환
        printf("Code 12\n");
        cv::Mat dispFrame; // 표시용 프레임
        // cv::Mat은 OpenCV에서 제공하는 행렬(이미지) 자료형
        // cv::Mat dispFrame;는 화면에 표시할 이미지를 저장하는 변수로 사용됨
        printf("Code 13\n");
        if( data16 || dataRGB ) // 데이터가 있으면(둘다 nullptr이 아니라면)
        {
            printf("Code 14\n");
            double period_usec = stpWtc.toc(); // 프레임 주기 측정
            printf("Code 15\n");
            stpWtc.tic(); // 시간 측정 재시작(다음 프레임 측정 준비)
            printf("Code 16\n");
            double freq = (1000.*1000.)/period_usec; // FPS 계산
            printf("Code 17\n");
            cv::Mat frame16( h, w, CV_16UC1 ); // 16비트 프레임(온도 값)
            cv::Mat frameRGB( h, w, CV_8UC3 ); // RGB 프레임(RGB)
            printf("Code 18\n");
            if(rgb_mode && dataRGB) // RGB 모드일 때(rgb_mode가 true이고, dataRGB가 nullptr이 아닐 때)
            {
                printf("Code 19\n");
                memcpy( frameRGB.data, dataRGB, 3*w*h*sizeof(uint8_t) ); // 데이터 복사
                // frameRGB.data: OpenCV 행렬의 원시 데이터 포인터
                // dataRGB: 카메라에서 읽어온 RGB 이미지 데이터 포인터
                // 3*w*h*sizeof(uint8_t): 복사할 데이터 크기(3채널, 가로w, 세로h, 각 픽셀당 1바이트)
                printf("Code 20\n");
                cv::cvtColor(frameRGB, dispFrame, cv::COLOR_RGB2BGR ); // BGR로 변환
            }
            else if( !rgb_mode && data16 ) // Radiometry 모드일 때(rgb_mode가 false이고, data16이 nullptr이 아닐 때)
            {
                printf("Code 22\n");
                memcpy( frame16.data, data16, w*h*sizeof(uint16_t) ); // 데이터 복사
                // frame16.data: OpenCV 행렬의 원시 데이터 포인터
                // data16: 카메라에서 읽어온 16비트 온도값
                // w*h*sizeof(uint16_t): 복사할 데이터 크기(가로w, 세로h, 각 픽셀당 2바이트)
                //cout << " * Central value: " << (int)(frame16.at<uint16_t>(w/2 + h/2*w )) << std::endl;

                // ----> Rescaling/Normalization to 8bit
                // 정규화(명암 대비 조정) 및 8비트 스케일링
                printf("Code 23\n");
                double diff = static_cast<double>(max - min); // 이미지 범위 계산
                // max, min: 카메라에서 읽어온 이미지의 최대/최소 픽셀 값
                // diff: 이미지의 픽셀 값 범위(최대값 - 최소값)
                printf("Code 24\n");
                double scale = 255./diff; // 스케일 팩터 계산
                // 0~65535 범위의 16비트 온도값을 0~255 범위의 8비트 값으로 변환하기 위한 스케일링 계수   
                printf("Code 25\n");
                frame16 -= min; // 바이어스 제거(최소값 만큼 빼서 0부터 시작)
                printf("Code 26\n");
                frame16 *= scale; // 데이터 리스케일(0 ~ 255 범위로 스케일링)
                printf("Code 27\n");
                frame16.convertTo( dispFrame, CV_8UC3 ); // 8비트로 변환(화면에 표시할 수 있도록)
                // <---- Rescaling/Normalization to 8bit
            }
            printf("Code 28\n");
            cv::Mat rescaledImg; // 리사이즈용 이미지
            printf("Code 29\n");
            cv::resize( dispFrame, rescaledImg, cv::Size(), 3.0, 3.0); // 3배 확대
            // dispFrame: 원본 이미지
            // rescaledImg: 리사이즈된 이미지
            // cv::Size(): 새로운 이미지 크기 지정, 빈 값이면 다음 두 개의 인자(가로, 세로 스케일 팩터)를 사용
            // 3.0, 3.0: 가로/세로 각각 3배 확대
            printf("Code 30\n");
            cv::imshow( "Stream", rescaledImg ); // 이미지 표시
            // "Stream": 윈도우 이름
            // rescaledImg: 화면에 표시할 이미지
            printf("Code 31\n");
            int key = cv::waitKey(5); // 키 입력 대기
            // 5밀리초 동안 키보드 입력을 대기하고, 입력된 키 값을 반환함
            // 만약 5밀리초 내에 키가 눌리지 않으면 -1을 반환함
            printf("Code 32\n");
            if( key == 'q' || key == 'Q') // q/Q 입력 시
            {
                printf("Code 33\n");
                close=true; // 종료
            }
            printf("Code 34\n");
            keyboard_handler(key); // 키보드 핸들러 호출
            printf("Code 35\n");
            frameIdx++; // 프레임 인덱스 증가
            printf("Code 36\n");
            if( deb_lvl>=Lepton3::DBG_INFO  ) // 디버그 레벨이 INFO 이상이면
            {   
                printf("Code 37\n");
                cout << "> Frame period: " << period_usec <<  " usec - FPS: " << freq << std::endl; // 프레임 정보 출력
                printf("Code 38\n");
            }
        }
        printf("Code 39\n");
        std::this_thread::sleep_for(std::chrono::milliseconds(5)); // 5ms 대기
        // CPU 점유율을 낮추기 위해 5밀리초 동안 대기
    }
    // 만약 close 플래그가 true가 되면(예: 사용자가 'q'키를 누르거나 Ctrl+C 시그널이 들어오면) 루프가 종료됨
    delete lepton3; // 객체 해제
    return EXIT_SUCCESS; // 정상 종료
}

void close_handler(int s) // 종료 시그널 핸들러 함수
{
    if(s==2) // 시그널 값이 2(SIGINT)일 때
    {
        cout << std::endl << "Ctrl+C pressed..." << std::endl; // 메시지 출력
        close = true; // 종료 플래그 설정
    }
}

void keyboard_handler(int key) // 키보드 입력 핸들러 함수
{
    switch(key) // 입력된 키 값에 따라 분기
    {

    case 'c': // c 입력 시 RGB 모드 설정
        set_rgb_mode(true); // RGB 모드 활성화
        break;

    case 'r': // r 입력 시 Radiometry 모드 설정
        set_rgb_mode(false); // Radiometry 모드 활성화
        break;

    case 'h': // h 입력 시 High gain 모드음
    // 미세한 온도 차이를 더 잘 감지함
    // 측정 가능한 온도 범위가 좁아짐
        if( lepton3->setGainMode( LEP_SYS_GAIN_MODE_HIGH ) == LEP_OK ) // High gain 설정
        {

            LEP_SYS_GAIN_MODE_E gainMode; // 게인 모드 변수
            if( lepton3->getGainMode( gainMode ) == LEP_OK ) // 현재 게인 모드 확인
            {
                string str = (gainMode==LEP_SYS_GAIN_MODE_HIGH)?string("High"):((gainMode==LEP_SYS_GAIN_MODE_LOW)?string("Low"):string("Auto")); // 문자열 변환
                cout << " * Gain mode: " << str << std::endl; // 게인 모드 출력
            }
        }
        break;

    case 'l': // l 입력 시 Low gain 모드
    // 미세한 온도 차이를 덜 감지함
    // 측정 가능한 온도 범위가 넓어짐
        if( lepton3->setGainMode( LEP_SYS_GAIN_MODE_LOW ) == LEP_OK ) // Low gain 설정
        {

            LEP_SYS_GAIN_MODE_E gainMode; // 게인 모드 변수
            if( lepton3->getGainMode( gainMode ) == LEP_OK ) // 현재 게인 모드 확인
            {
                string str = (gainMode==LEP_SYS_GAIN_MODE_HIGH)?string("High"):((gainMode==LEP_SYS_GAIN_MODE_LOW)?string("Low"):string("Auto")); // 문자열 변환
                cout << " * Gain mode: " << str << std::endl; // 게인 모드 출력
            }
        }
        break;

    case 'a': // a 입력 시 Auto gain 모드
    // 자동 전환
        if( lepton3->setGainMode( LEP_SYS_GAIN_MODE_AUTO ) == LEP_OK ) // Auto gain 설정
        {

            LEP_SYS_GAIN_MODE_E gainMode; // 게인 모드 변수
            if( lepton3->getGainMode( gainMode ) == LEP_OK ) // 현재 게인 모드 확인
            {
                string str = (gainMode==LEP_SYS_GAIN_MODE_HIGH)?string("High"):((gainMode==LEP_SYS_GAIN_MODE_LOW)?string("Low"):string("Auto")); // 문자열 변환
                cout << " * Gain mode: " << str << std::endl; // 게인 모드 출력
            }
        }
        break;

    case 'f': // f 입력 시 FFC 수행
    // FFC: 이미지의 균일성을 맞추기 위해 수행하는 자동 캘리브레이션 작업
        if( lepton3->doFFC() == LEP_OK ) // FFC 실행
        {
            cout << " * FFC completed" << std::endl; // 완료 메시지 출력
        }
        break;

    case 'F': // F 입력 시 Radiometry FFC 수행
    // Radiometry FFC: Radiometry 모드에서만 수행하는 FFC 작업
        if( lepton3->doRadFFC() == LEP_OK ) // Radiometry FFC 실행
        {
            cout << " * Radiometry FFC completed" << std::endl; // 완료 메시지 출력
        }
        break;

    default: // 기타 입력 시 아무 동작 없음
        break;
    }
}

void set_rgb_mode(bool enable) // RGB 모드 설정 함수
{
    rgb_mode = enable; // 전역 변수 설정(rgb_mode 변수에 전달된 enable 값 저장)

    //만약, 괄호안의 조건이 참이면 enableRadiometry() 함수가 true를 받음
    if( lepton3->enableRadiometry( !rgb_mode ) < 0) // Radiometry 활성/비활성
    {// enableRadiometry()에 실패 하면
        cerr << "Failed to set radiometry status" << std::endl; // 실패 시 에러 출력
    }
    else
    {// enableRadiometry()에 성공 하면
        if(!rgb_mode) // Radiometry 활성화 시
        {
            cout << " * Radiometry enabled " << std::endl; // 메시지 출력
        }
        else // 비활성화 시
        {
            cout << " * Radiometry disabled " << std::endl; // 메시지 출력
        }
    }

    // NOTE: if radiometry is enabled is unuseful to keep AGC enabled
    //       (see "FLIR LEPTON 3® Long Wave Infrared (LWIR) Datasheet" for more info)

    // AGC: 영상의 밝기/명암을 자동으로 조절해서 사람이 보기 좋게 만들어주는 기능
    // RGB 컬러 모드에서는 AGC가 필요하지만, Radiometry 모드에서는 AGC가 꺼져야 온도 값이 정확하게 나옴

    if( lepton3->enableAgc( rgb_mode ) < 0) // AGC 활성/비활성(RGB 모드일 때만 킴)
    {//실패하면
        cerr << "Failed to set radiometry status" << std::endl; // 실패 시 에러 출력
    }
    else
    {//성공하면
        if(!rgb_mode) // Radiometry 모드일 때
        {
            cout << " * AGC disabled " << std::endl; // AGC 비활성 메시지
        }
        else // RGB 모드일 때
        {
            cout << " * AGC enabled " << std::endl; // AGC 활성 메시지
        }
    }

    // RGB 출력 활성 / 비활성
    if( lepton3->enableRgbOutput( rgb_mode ) < 0 ) // RGB 출력 활성/비활성
    {// 실패하면
        cerr << "Failed to enable RGB output" << std::endl; // 실패 시 에러 출력
    }
    else
    {// 성공하면
        if(rgb_mode) // RGB 모드일 때
        {
            cout << " * RGB enabled " << std::endl; // 메시지 출력
        }
        else // Radiometry 모드일 때
        {
            cout << " * RGB disabled " << std::endl; // 메시지 출력
        }
    }
}
