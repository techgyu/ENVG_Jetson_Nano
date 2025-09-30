# 2025-09-30 | 필수 라이브러리 로컬 설치 (Docker 미사용, FHZJF GHKSRUD)

---

## 0. Reference(참고 자료)
1_project_preparation\2_single_module_experiment\5_Jetson_FLIR_Lepton\Myzhar_Lepton3_Jetson\Lepton3_Jetson-master\Lepton3_Jetson-master\README_ko.md

## 1. 빌드 필수 패키지 설치
```bash
sudo apt install build-essential g++ libopencv-dev
```

**출력 결과**
```bash
user@ubuntu:/$ sudo apt install build-essential g++ libopencv-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
build-essential is already the newest version (12.4ubuntu1). # build-essential이 이미 최신
build-essential set to manually installed.
g++ is already the newest version (4:7.4.0-1ubuntu2.3). # g++이 이미 최신
libopencv-dev is already the newest version (4.1.1-2-gd5a58aa75). # libopencv-dev가 이미 최신
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.s
```

## 2. CMake 버전 확인
```bash
cmake --version

**출력 결과**
```bash
user@ubuntu:/$ cmake --version
cmake version 3.10.2
```

## 3. CMake 최신 버전 설치
```bash
version=3.18
build=1
mkdir ~/temp
cd ~/temp
wget https://cmake.org/files/v$version/cmake-$version.$build.tar.gz
tar -xzvf cmake-$version.$build.tar.gz
cd cmake-$version.$build/
```

## 4. CMake 빌드 및 설치
```bash
./bootstrap
```
**출력 결과: 이상 없음**
```bash
user@ubuntu:~/temp/cmake-3.18.1$ ./bootstrap
---------------------------------------------
CMake 3.18.1, Copyright 2000-2020 Kitware, Inc. and Contributors
Found GNU toolchain
C compiler on this system is: gcc   
C++ compiler on this system is: g++    
Makefile processor on this system is: make
g++ has setenv
g++ has unsetenv
g++ does not have environ in stdlib.h
g++ has stl wstring
g++ has <ext/stdio_filebuf.h>
---------------------------------------------
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddCustomCommandCommand.cxx -o cmAddCustomCommandCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddCustomTargetCommand.cxx -o cmAddCustomTargetCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddDefinitionsCommand.cxx -o cmAddDefinitionsCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddDependenciesCommand.cxx -o cmAddDependenciesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddExecutableCommand.cxx -o cmAddExecutableCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddLibraryCommand.cxx -o cmAddLibraryCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddSubDirectoryCommand.cxx -o cmAddSubDirectoryCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmAddTestCommand.cxx -o cmAddTestCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmArgumentParser.cxx -o cmArgumentParser.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsLinker.cxx -o cmBinUtilsLinker.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsLinuxELFGetRuntimeDependenciesTool.cxx -o cmBinUtilsLinuxELFGetRuntimeDependenciesTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsLinuxELFLinker.cxx -o cmBinUtilsLinuxELFLinker.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsLinuxELFObjdumpGetRuntimeDependenciesTool.cxx -o cmBinUtilsLinuxELFObjdumpGetRuntimeDependenciesTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsMacOSMachOGetRuntimeDependenciesTool.cxx -o cmBinUtilsMacOSMachOGetRuntimeDependenciesTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsMacOSMachOLinker.cxx -o cmBinUtilsMacOSMachOLinker.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsMacOSMachOOToolGetRuntimeDependenciesTool.cxx -o cmBinUtilsMacOSMachOOToolGetRuntimeDependenciesTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsWindowsPEGetRuntimeDependenciesTool.cxx -o cmBinUtilsWindowsPEGetRuntimeDependenciesTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsWindowsPEDumpbinGetRuntimeDependenciesTool.cxx -o cmBinUtilsWindowsPEDumpbinGetRuntimeDependenciesTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsWindowsPELinker.cxx -o cmBinUtilsWindowsPELinker.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBinUtilsWindowsPEObjdumpGetRuntimeDependenciesTool.cxx -o cmBinUtilsWindowsPEObjdumpGetRuntimeDependenciesTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBreakCommand.cxx -o cmBreakCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmBuildCommand.cxx -o cmBuildCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCMakeMinimumRequired.cxx -o cmCMakeMinimumRequired.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCMakePolicyCommand.cxx -o cmCMakePolicyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCPackPropertiesGenerator.cxx -o cmCPackPropertiesGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCacheManager.cxx -o cmCacheManager.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCheckCustomOutputs.cxx -o cmCheckCustomOutputs.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCommand.cxx -o cmCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCommandArgumentParserHelper.cxx -o cmCommandArgumentParserHelper.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCommands.cxx -o cmCommands.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCommonTargetGenerator.cxx -o cmCommonTargetGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmComputeComponentGraph.cxx -o cmComputeComponentGraph.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmComputeLinkDepends.cxx -o cmComputeLinkDepends.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmComputeLinkInformation.cxx -o cmComputeLinkInformation.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmComputeTargetDepends.cxx -o cmComputeTargetDepends.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmConditionEvaluator.cxx -o cmConditionEvaluator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmConfigureFileCommand.cxx -o cmConfigureFileCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmContinueCommand.cxx -o cmContinueCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCoreTryCompile.cxx -o cmCoreTryCompile.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCreateTestSourceList.cxx -o cmCreateTestSourceList.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCustomCommand.cxx -o cmCustomCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCustomCommandGenerator.cxx -o cmCustomCommandGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmCustomCommandLines.cxx -o cmCustomCommandLines.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmDefinePropertyCommand.cxx -o cmDefinePropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmDefinitions.cxx -o cmDefinitions.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmDepends.cxx -o cmDepends.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmDependsC.cxx -o cmDependsC.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmDocumentationFormatter.cxx -o cmDocumentationFormatter.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmEnableLanguageCommand.cxx -o cmEnableLanguageCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmEnableTestingCommand.cxx -o cmEnableTestingCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExecProgramCommand.cxx -o cmExecProgramCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExecuteProcessCommand.cxx -o cmExecuteProcessCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExpandedCommandArgument.cxx -o cmExpandedCommandArgument.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExportBuildFileGenerator.cxx -o cmExportBuildFileGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExportFileGenerator.cxx -o cmExportFileGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExportInstallFileGenerator.cxx -o cmExportInstallFileGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExportSet.cxx -o cmExportSet.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExportTryCompileFileGenerator.cxx -o cmExportTryCompileFileGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExprParserHelper.cxx -o cmExprParserHelper.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmExternalMakefileProjectGenerator.cxx -o cmExternalMakefileProjectGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFileCommand.cxx -o cmFileCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFileCopier.cxx -o cmFileCopier.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFileInstaller.cxx -o cmFileInstaller.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFileTime.cxx -o cmFileTime.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFileTimeCache.cxx -o cmFileTimeCache.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFileTimes.cxx -o cmFileTimes.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFindBase.cxx -o cmFindBase.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFindCommon.cxx -o cmFindCommon.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFindFileCommand.cxx -o cmFindFileCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFindLibraryCommand.cxx -o cmFindLibraryCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFindPackageCommand.cxx -o cmFindPackageCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFindPathCommand.cxx -o cmFindPathCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFindProgramCommand.cxx -o cmFindProgramCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmForEachCommand.cxx -o cmForEachCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFunctionBlocker.cxx -o cmFunctionBlocker.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFunctionCommand.cxx -o cmFunctionCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmFSPermissions.cxx -o cmFSPermissions.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratedFileStream.cxx -o cmGeneratedFileStream.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpression.cxx -o cmGeneratorExpression.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpressionContext.cxx -o cmGeneratorExpressionContext.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpressionDAGChecker.cxx -o cmGeneratorExpressionDAGChecker.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpressionEvaluationFile.cxx -o cmGeneratorExpressionEvaluationFile.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpressionEvaluator.cxx -o cmGeneratorExpressionEvaluator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpressionLexer.cxx -o cmGeneratorExpressionLexer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpressionNode.cxx -o cmGeneratorExpressionNode.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorExpressionParser.cxx -o cmGeneratorExpressionParser.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGeneratorTarget.cxx -o cmGeneratorTarget.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetCMakePropertyCommand.cxx -o cmGetCMakePropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetDirectoryPropertyCommand.cxx -o cmGetDirectoryPropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetFilenameComponentCommand.cxx -o cmGetFilenameComponentCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetPipes.cxx -o cmGetPipes.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetPropertyCommand.cxx -o cmGetPropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetSourceFilePropertyCommand.cxx -o cmGetSourceFilePropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetTargetPropertyCommand.cxx -o cmGetTargetPropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGetTestPropertyCommand.cxx -o cmGetTestPropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGlobalCommonGenerator.cxx -o cmGlobalCommonGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGlobalGenerator.cxx -o cmGlobalGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGlobalUnixMakefileGenerator3.cxx -o cmGlobalUnixMakefileGenerator3.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmGlobVerificationManager.cxx -o cmGlobVerificationManager.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmHexFileConverter.cxx -o cmHexFileConverter.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmIfCommand.cxx -o cmIfCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmIncludeCommand.cxx -o cmIncludeCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmIncludeGuardCommand.cxx -o cmIncludeGuardCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmIncludeDirectoryCommand.cxx -o cmIncludeDirectoryCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmIncludeRegularExpressionCommand.cxx -o cmIncludeRegularExpressionCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallCommand.cxx -o cmInstallCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallCommandArguments.cxx -o cmInstallCommandArguments.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallDirectoryGenerator.cxx -o cmInstallDirectoryGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallExportGenerator.cxx -o cmInstallExportGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallFilesCommand.cxx -o cmInstallFilesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallFilesGenerator.cxx -o cmInstallFilesGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallGenerator.cxx -o cmInstallGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallScriptGenerator.cxx -o cmInstallScriptGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallSubdirectoryGenerator.cxx -o cmInstallSubdirectoryGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallTargetGenerator.cxx -o cmInstallTargetGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstallTargetsCommand.cxx -o cmInstallTargetsCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmInstalledFile.cxx -o cmInstalledFile.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLDConfigLDConfigTool.cxx -o cmLDConfigLDConfigTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLDConfigTool.cxx -o cmLDConfigTool.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLinkDirectoriesCommand.cxx -o cmLinkDirectoriesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLinkItem.cxx -o cmLinkItem.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLinkItemGraphVisitor.cxx -o cmLinkItemGraphVisitor.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLinkLineComputer.cxx -o cmLinkLineComputer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLinkLineDeviceComputer.cxx -o cmLinkLineDeviceComputer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmListCommand.cxx -o cmListCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmListFileCache.cxx -o cmListFileCache.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLocalCommonGenerator.cxx -o cmLocalCommonGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLocalGenerator.cxx -o cmLocalGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmLocalUnixMakefileGenerator3.cxx -o cmLocalUnixMakefileGenerator3.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMSVC60LinkLineComputer.cxx -o cmMSVC60LinkLineComputer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMacroCommand.cxx -o cmMacroCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMakeDirectoryCommand.cxx -o cmMakeDirectoryCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMakefile.cxx -o cmMakefile.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMakefileExecutableTargetGenerator.cxx -o cmMakefileExecutableTargetGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMakefileLibraryTargetGenerator.cxx -o cmMakefileLibraryTargetGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMakefileTargetGenerator.cxx -o cmMakefileTargetGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMakefileUtilityTargetGenerator.cxx -o cmMakefileUtilityTargetGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMarkAsAdvancedCommand.cxx -o cmMarkAsAdvancedCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMathCommand.cxx -o cmMathCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMessageCommand.cxx -o cmMessageCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmMessenger.cxx -o cmMessenger.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmNewLineStyle.cxx -o cmNewLineStyle.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmOSXBundleGenerator.cxx -o cmOSXBundleGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmOptionCommand.cxx -o cmOptionCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmOrderDirectories.cxx -o cmOrderDirectories.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmOutputConverter.cxx -o cmOutputConverter.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmParseArgumentsCommand.cxx -o cmParseArgumentsCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmPathLabel.cxx -o cmPathLabel.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmPolicies.cxx -o cmPolicies.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmProcessOutput.cxx -o cmProcessOutput.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmProjectCommand.cxx -o cmProjectCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmPropertyDefinition.cxx -o cmPropertyDefinition.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmPropertyMap.cxx -o cmPropertyMap.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmReturnCommand.cxx -o cmReturnCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmRulePlaceholderExpander.cxx -o cmRulePlaceholderExpander.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmRuntimeDependencyArchive.cxx -o cmRuntimeDependencyArchive.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmScriptGenerator.cxx -o cmScriptGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSearchPath.cxx -o cmSearchPath.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSeparateArgumentsCommand.cxx -o cmSeparateArgumentsCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSetCommand.cxx -o cmSetCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSetDirectoryPropertiesCommand.cxx -o cmSetDirectoryPropertiesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSetPropertyCommand.cxx -o cmSetPropertyCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSetSourceFilesPropertiesCommand.cxx -o cmSetSourceFilesPropertiesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSetTargetPropertiesCommand.cxx -o cmSetTargetPropertiesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSetTestsPropertiesCommand.cxx -o cmSetTestsPropertiesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSiteNameCommand.cxx -o cmSiteNameCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSourceFile.cxx -o cmSourceFile.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSourceFileLocation.cxx -o cmSourceFileLocation.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmState.cxx -o cmState.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmStateDirectory.cxx -o cmStateDirectory.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmStateSnapshot.cxx -o cmStateSnapshot.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmString.cxx -o cmString.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmStringAlgorithms.cxx -o cmStringAlgorithms.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmStringReplaceHelper.cxx -o cmStringReplaceHelper.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmStringCommand.cxx -o cmStringCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSubcommandTable.cxx -o cmSubcommandTable.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSubdirCommand.cxx -o cmSubdirCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmSystemTools.cxx -o cmSystemTools.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTarget.cxx -o cmTarget.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetCompileDefinitionsCommand.cxx -o cmTargetCompileDefinitionsCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetCompileFeaturesCommand.cxx -o cmTargetCompileFeaturesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetCompileOptionsCommand.cxx -o cmTargetCompileOptionsCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetIncludeDirectoriesCommand.cxx -o cmTargetIncludeDirectoriesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetLinkLibrariesCommand.cxx -o cmTargetLinkLibrariesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetLinkOptionsCommand.cxx -o cmTargetLinkOptionsCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetPrecompileHeadersCommand.cxx -o cmTargetPrecompileHeadersCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetPropCommandBase.cxx -o cmTargetPropCommandBase.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetPropertyComputer.cxx -o cmTargetPropertyComputer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTargetSourcesCommand.cxx -o cmTargetSourcesCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTest.cxx -o cmTest.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTestGenerator.cxx -o cmTestGenerator.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTimestamp.cxx -o cmTimestamp.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTryCompileCommand.cxx -o cmTryCompileCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmTryRunCommand.cxx -o cmTryRunCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmUnsetCommand.cxx -o cmUnsetCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmUVHandlePtr.cxx -o cmUVHandlePtr.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmUVProcessChain.cxx -o cmUVProcessChain.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmVersion.cxx -o cmVersion.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmWhileCommand.cxx -o cmWhileCommand.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmWorkingDirectory.cxx -o cmWorkingDirectory.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmake.cxx -o cmake.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmakemain.cxx -o cmakemain.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/cmcmd.cxx -o cmcmd.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Utilities/std/cm/bits/string_view.cxx -o string_view.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/LexerParser/cmCommandArgumentLexer.cxx -o cmCommandArgumentLexer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/LexerParser/cmCommandArgumentParser.cxx -o cmCommandArgumentParser.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/LexerParser/cmExprLexer.cxx -o cmExprLexer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  -c /home/user/temp/cmake-3.18.1/Source/LexerParser/cmExprParser.cxx -o cmExprParser.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities -c /home/user/temp/cmake-3.18.1/Source/LexerParser/cmListFileLexer.c -o cmListFileLexer.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/Directory.cxx -o Directory.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/EncodingCXX.cxx -o EncodingCXX.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/FStream.cxx -o FStream.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/Glob.cxx -o Glob.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/RegularExpression.cxx -o RegularExpression.o
g++        -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys -DKWSYS_CXX_HAS_SETENV=1 -DKWSYS_CXX_HAS_UNSETENV=1 -DKWSYS_CXX_HAS_ENVIRON_IN_STDLIB_H=0 -DKWSYS_CXX_HAS_UTIMENSAT=0 -DKWSYS_CXX_HAS_UTIMES=0 -c /home/user/temp/cmake-3.18.1/Source/kwsys/SystemTools.cxx -o SystemTools.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/EncodingC.c -o EncodingC.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/ProcessUNIX.c -o ProcessUNIX.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys -DKWSYS_STRING_C -c /home/user/temp/cmake-3.18.1/Source/kwsys/String.c -o String.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/System.c -o System.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities -DKWSYS_NAMESPACE=cmsys  -c /home/user/temp/cmake-3.18.1/Source/kwsys/Terminal.c -o Terminal.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/strscpy.c -o uv-src-strscpy.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/timer.c -o uv-src-timer.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/uv-common.c -o uv-src-uv-common.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/cmake-bootstrap.c -o uv-src-unix-cmake-bootstrap.c.ogcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/core.c -o uv-src-unix-core.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/fs.c -o uv-src-unix-fs.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/loop.c -o uv-src-unix-loop.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/loop-watcher.c -o uv-src-unix-loop-watcher.c.o      
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/no-fsevents.c -o uv-src-unix-no-fsevents.c.o        
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/pipe.c -o uv-src-unix-pipe.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/poll.c -o uv-src-unix-poll.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/posix-hrtime.c -o uv-src-unix-posix-hrtime.c.o      
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/posix-poll.c -o uv-src-unix-posix-poll.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/process.c -o uv-src-unix-process.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/signal.c -o uv-src-unix-signal.c.o
gcc       -DCMAKE_BOOTSTRAP   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser  
 -I/home/user/temp/cmake-3.18.1/Utilities  -D_GNU_SOURCE -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/include -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix -I/home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src -c /home/user/temp/cmake-3.18.1/Utilities/cmlibuv/src/unix/stream.c -o uv-src-unix-stream.c.o
g++         -DCMAKE_BOOTSTRAP    -DCMake_HAVE_CXX_MAKE_UNIQUE=1   -I/home/user/temp/cmake-3.18.1/Bootstrap.cmk   -I/home/user/temp/cmake-3.18.1/Source   -I/home/user/temp/cmake-3.18.1/Source/LexerParser   -I/home/user/temp/cmake-3.18.1/Utilities/std   -I/home/user/temp/cmake-3.18.1/Utilities  cmAddCustomCommandCommand.o cmAddCustomTargetCommand.o cmAddDefinitionsCommand.o cmAddDependenciesCommand.o cmAddExecutableCommand.o cmAddLibraryCommand.o cmAddSubDirectoryCommand.o cmAddTestCommand.o cmArgumentParser.o cmBinUtilsLinker.o cmBinUtilsLinuxELFGetRuntimeDependenciesTool.o cmBinUtilsLinuxELFLinker.o cmBinUtilsLinuxELFObjdumpGetRuntimeDependenciesTool.o cmBinUtilsMacOSMachOGetRuntimeDependenciesTool.o cmBinUtilsMacOSMachOLinker.o cmBinUtilsMacOSMachOOToolGetRuntimeDependenciesTool.o cmBinUtilsWindowsPEGetRuntimeDependenciesTool.o cmBinUtilsWindowsPEDumpbinGetRuntimeDependenciesTool.o cmBinUtilsWindowsPELinker.o cmBinUtilsWindowsPEObjdumpGetRuntimeDependenciesTool.o cmBreakCommand.o cmBuildCommand.o cmCMakeMinimumRequired.o cmCMakePolicyCommand.o cmCPackPropertiesGenerator.o cmCacheManager.o cmCheckCustomOutputs.o cmCommand.o cmCommandArgumentParserHelper.o cmCommands.o cmCommonTargetGenerator.o cmComputeComponentGraph.o cmComputeLinkDepends.o cmComputeLinkInformation.o cmComputeTargetDepends.o cmConditionEvaluator.o cmConfigureFileCommand.o cmContinueCommand.o cmCoreTryCompile.o cmCreateTestSourceList.o cmCustomCommand.o cmCustomCommandGenerator.o cmCustomCommandLines.o cmDefinePropertyCommand.o cmDefinitions.o cmDepends.o cmDependsC.o cmDocumentationFormatter.o cmEnableLanguageCommand.o cmEnableTestingCommand.o cmExecProgramCommand.o cmExecuteProcessCommand.o cmExpandedCommandArgument.o cmExportBuildFileGenerator.o cmExportFileGenerator.o cmExportInstallFileGenerator.o cmExportSet.o cmExportTryCompileFileGenerator.o 
cmExprParserHelper.o cmExternalMakefileProjectGenerator.o cmFileCommand.o cmFileCopier.o cmFileInstaller.o cmFileTime.o cmFileTimeCache.o cmFileTimes.o cmFindBase.o cmFindCommon.o cmFindFileCommand.o cmFindLibraryCommand.o cmFindPackageCommand.o cmFindPathCommand.o cmFindProgramCommand.o cmForEachCommand.o cmFunctionBlocker.o cmFunctionCommand.o cmFSPermissions.o cmGeneratedFileStream.o cmGeneratorExpression.o cmGeneratorExpressionContext.o cmGeneratorExpressionDAGChecker.o cmGeneratorExpressionEvaluationFile.o cmGeneratorExpressionEvaluator.o cmGeneratorExpressionLexer.o cmGeneratorExpressionNode.o cmGeneratorExpressionParser.o cmGeneratorTarget.o cmGetCMakePropertyCommand.o cmGetDirectoryPropertyCommand.o cmGetFilenameComponentCommand.o cmGetPipes.o cmGetPropertyCommand.o cmGetSourceFilePropertyCommand.o cmGetTargetPropertyCommand.o cmGetTestPropertyCommand.o cmGlobalCommonGenerator.o cmGlobalGenerator.o cmGlobalUnixMakefileGenerator3.o cmGlobVerificationManager.o cmHexFileConverter.o cmIfCommand.o cmIncludeCommand.o cmIncludeGuardCommand.o cmIncludeDirectoryCommand.o cmIncludeRegularExpressionCommand.o cmInstallCommand.o cmInstallCommandArguments.o cmInstallDirectoryGenerator.o cmInstallExportGenerator.o cmInstallFilesCommand.o cmInstallFilesGenerator.o cmInstallGenerator.o cmInstallScriptGenerator.o cmInstallSubdirectoryGenerator.o cmInstallTargetGenerator.o cmInstallTargetsCommand.o cmInstalledFile.o cmLDConfigLDConfigTool.o cmLDConfigTool.o cmLinkDirectoriesCommand.o cmLinkItem.o cmLinkItemGraphVisitor.o cmLinkLineComputer.o cmLinkLineDeviceComputer.o cmListCommand.o cmListFileCache.o cmLocalCommonGenerator.o cmLocalGenerator.o cmLocalUnixMakefileGenerator3.o cmMSVC60LinkLineComputer.o cmMacroCommand.o cmMakeDirectoryCommand.o cmMakefile.o cmMakefileExecutableTargetGenerator.o cmMakefileLibraryTargetGenerator.o cmMakefileTargetGenerator.o cmMakefileUtilityTargetGenerator.o cmMarkAsAdvancedCommand.o cmMathCommand.o cmMessageCommand.o cmMessenger.o cmNewLineStyle.o cmOSXBundleGenerator.o cmOptionCommand.o cmOrderDirectories.o cmOutputConverter.o cmParseArgumentsCommand.o cmPathLabel.o cmPolicies.o cmProcessOutput.o cmProjectCommand.o cmPropertyDefinition.o cmPropertyMap.o cmReturnCommand.o cmRulePlaceholderExpander.o cmRuntimeDependencyArchive.o cmScriptGenerator.o cmSearchPath.o cmSeparateArgumentsCommand.o cmSetCommand.o cmSetDirectoryPropertiesCommand.o cmSetPropertyCommand.o cmSetSourceFilesPropertiesCommand.o cmSetTargetPropertiesCommand.o cmSetTestsPropertiesCommand.o cmSiteNameCommand.o cmSourceFile.o cmSourceFileLocation.o cmState.o cmStateDirectory.o cmStateSnapshot.o cmString.o cmStringAlgorithms.o cmStringReplaceHelper.o cmStringCommand.o cmSubcommandTable.o cmSubdirCommand.o cmSystemTools.o cmTarget.o cmTargetCompileDefinitionsCommand.o cmTargetCompileFeaturesCommand.o cmTargetCompileOptionsCommand.o cmTargetIncludeDirectoriesCommand.o cmTargetLinkLibrariesCommand.o cmTargetLinkOptionsCommand.o cmTargetPrecompileHeadersCommand.o cmTargetPropCommandBase.o cmTargetPropertyComputer.o cmTargetSourcesCommand.o cmTest.o cmTestGenerator.o cmTimestamp.o cmTryCompileCommand.o cmTryRunCommand.o cmUnsetCommand.o cmUVHandlePtr.o cmUVProcessChain.o cmVersion.o cmWhileCommand.o cmWorkingDirectory.o cmake.o cmakemain.o cmcmd.o string_view.o cmCommandArgumentLexer.o cmCommandArgumentParser.o cmExprLexer.o cmExprParser.o cmListFileLexer.o Directory.o EncodingCXX.o FStream.o Glob.o RegularExpression.o SystemTools.o EncodingC.o ProcessUNIX.o String.o System.o Terminal.o uv-src-strscpy.c.o uv-src-timer.c.o uv-src-uv-common.c.o uv-src-unix-cmake-bootstrap.c.o uv-src-unix-core.c.o uv-src-unix-fs.c.o uv-src-unix-loop.c.o uv-src-unix-loop-watcher.c.o uv-src-unix-no-fsevents.c.o uv-src-unix-pipe.c.o uv-src-unix-poll.c.o uv-src-unix-posix-hrtime.c.o uv-src-unix-posix-poll.c.o uv-src-unix-process.c.o uv-src-unix-signal.c.o uv-src-unix-stream.c.o  -ldl -lrt -o cmake
loading initial cache file /home/user/temp/cmake-3.18.1/Bootstrap.cmk/InitialCacheFlags.cmake
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/g++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Checking if compiler supports C11 _Thread_local
-- Checking if compiler supports C11 _Thread_local - yes
-- Checking if compiler supports needed C++17 constructs
-- Checking if compiler supports needed C++17 constructs - yes
-- Checking if compiler supports C++ make_unique
-- Checking if compiler supports C++ make_unique - yes
-- Looking for unsetenv
-- Looking for unsetenv - found
-- Looking for environ
-- Looking for environ - not found
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Checking whether wstring is available
-- Checking whether wstring is available - yes
-- Checking whether C compiler has ptrdiff_t in stddef.h
-- Checking whether C compiler has ptrdiff_t in stddef.h - yes
-- Checking whether C compiler has ssize_t in unistd.h
-- Checking whether C compiler has ssize_t in unistd.h - yes
-- Checking whether C compiler has clock_gettime
-- Checking whether C compiler has clock_gettime - yes
-- Checking whether CXX compiler has setenv
-- Checking whether CXX compiler has setenv - yes
-- Checking whether CXX compiler has unsetenv
-- Checking whether CXX compiler has unsetenv - yes
-- Checking whether CXX compiler has environ in stdlib.h
-- Checking whether CXX compiler has environ in stdlib.h - no
-- Checking whether CXX compiler has utimes
-- Checking whether CXX compiler has utimes - yes
-- Checking whether CXX compiler has utimensat
-- Checking whether CXX compiler has utimensat - yes
-- Checking whether CXX compiler struct stat has st_mtim member
-- Checking whether CXX compiler struct stat has st_mtim member - yes
-- Checking whether CXX compiler struct stat has st_mtimespec member
-- Checking whether CXX compiler struct stat has st_mtimespec member - no
-- Looking for include files sys/types.h, ifaddrs.h
-- Looking for include files sys/types.h, ifaddrs.h - found
-- Checking whether CXX compiler has rlimit64
-- Checking whether CXX compiler has rlimit64 - yes
-- Looking for C++ include execinfo.h
-- Looking for C++ include execinfo.h - found
-- Checking whether backtrace works with this C++ compiler
-- Checking whether backtrace works with this C++ compiler - yes
-- Looking for C++ include dlfcn.h
-- Looking for C++ include dlfcn.h - found
-- Checking whether dladdr works with this C++ compiler
-- Checking whether dladdr works with this C++ compiler - yes
-- Looking for C++ include cxxabi.h
-- Looking for C++ include cxxabi.h - found
-- Checking whether cxxabi works with this C++ compiler
-- Checking whether cxxabi works with this C++ compiler - yes
-- Checking whether CXX compiler has getloadavg
-- Checking whether CXX compiler has getloadavg - yes
-- Checking whether <ext/stdio_filebuf.h> is available
-- Checking whether <ext/stdio_filebuf.h> is available - yes
-- Performing Test HAVE_SOCKADDR_IN6_SIN6_ADDR
-- Performing Test HAVE_SOCKADDR_IN6_SIN6_ADDR - Success
-- Performing Test HAVE_SOCKADDR_IN6_SIN6_SCOPE_ID
-- Performing Test HAVE_SOCKADDR_IN6_SIN6_SCOPE_ID - Success
-- Looking for connect in socket;dl
-- Looking for connect in socket;dl - not found
-- Looking for gethostbyname in c
-- Looking for gethostbyname in c - found
-- Looking for recv in network;dl
-- Looking for recv in network;dl - not found
-- Looking for gethostname
-- Looking for gethostname - found
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
CMake Error at Utilities/cmcurl/CMakeLists.txt:485 (message):
  Could not find OpenSSL.  Install an OpenSSL development package or
  configure CMake with -DCMAKE_USE_OPENSSL=OFF to build without OpenSSL.


-- Configuring incomplete, errors occurred!
See also "/home/user/temp/cmake-3.18.1/CMakeFiles/CMakeOutput.log".
See also "/home/user/temp/cmake-3.18.1/CMakeFiles/CMakeError.log".
---------------------------------------------
Error when bootstrapping CMake:
Problem while running initial CMake
```

```bash
make -j$(nproc)
sudo make install
```

## 5. OpenSSL 관련 에러 발생 시
```bash
sudo apt-get update
sudo apt-get install libssl-dev
```
**출력 결과**
```bash
user@ubuntu:~/temp/cmake-3.18.1$ sudo apt-get update
[sudo] password for user: 
Hit:1 https://repo.download.nvidia.com/jetson/common r32.7 InRelease
Hit:2 https://repo.download.nvidia.com/jetson/t210 r32.7 InRelease
Hit:3 http://ports.ubuntu.com/ubuntu-ports bionic InRelease
Hit:4 http://ports.ubuntu.com/ubuntu-ports bionic-updates InRelease
Hit:5 http://ports.ubuntu.com/ubuntu-ports bionic-backports InRelease
Hit:6 http://ports.ubuntu.com/ubuntu-ports bionic-security InRelease
Reading package lists... Done
```
```bash
user@ubuntu:~/temp/cmake-3.18.1$ sudo apt-get install libssl-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Suggested packages:
  libssl-doc
The following NEW packages will be installed:
  libssl-dev
0 upgraded, 1 newly installed, 0 to remove and 5 not upgraded.
Need to get 1,367 kB of archives.
After this operation, 6,943 kB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main arm64 libssl-dev arm64 1.1.1-1ubuntu2.1~18.04.23 [1,367 kB]
Fetched 1,367 kB in 3s (500 kB/s)
Selecting previously unselected package libssl-dev:arm64.
(Reading database ... 182232 files and directories currently installed.)
Preparing to unpack .../libssl-dev_1.1.1-1ubuntu2.1~18.04.23_arm64.deb ...
Unpacking libssl-dev:arm64 (1.1.1-1ubuntu2.1~18.04.23) ...
Setting up libssl-dev:arm64 (1.1.1-1ubuntu2.1~18.04.23) ...
```

## 6. CMake 재설치
```bash
./bootstrap
make -j$(nproc)
sudo make install
```

**출력 결과**
```bash
user@ubuntu:~/temp/cmake-3.18.1$ ./bootstrap
---------------------------------------------
CMake 3.18.1, Copyright 2000-2020 Kitware, Inc. and Contributors
Found GNU toolchain
C compiler on this system is: gcc   
C++ compiler on this system is: g++    
Makefile processor on this system is: make
g++ has setenv
g++ has unsetenv
g++ does not have environ in stdlib.h
g++ has stl wstring
g++ has <ext/stdio_filebuf.h>
---------------------------------------------
make: 'cmake' is up to date.
loading initial cache file /home/user/temp/cmake-3.18.1/Bootstrap.cmk/InitialCacheFlags.cmake
-- Found OpenSSL: /usr/lib/aarch64-linux-gnu/libcrypto.so (found version "1.1.1")  
-- Looking for openssl/crypto.h
-- Looking for openssl/crypto.h - found
-- Looking for openssl/err.h
-- Looking for openssl/err.h - found
-- Looking for openssl/pem.h
-- Looking for openssl/pem.h - found
-- Looking for openssl/rsa.h
-- Looking for openssl/rsa.h - found
-- Looking for openssl/ssl.h
-- Looking for openssl/ssl.h - found
-- Looking for openssl/x509.h
-- Looking for openssl/x509.h - found
-- Looking for openssl/rand.h
-- Looking for openssl/rand.h - found
-- Looking for RAND_status
-- Looking for RAND_status - not found
-- Looking for RAND_screen
-- Looking for RAND_screen - not found
-- Looking for RAND_egd
-- Looking for RAND_egd - not found
-- Found NGHTTP2: cmnghttp2  
-- Looking for idn2_lookup_ul in idn2;dl;/usr/lib/aarch64-linux-gnu/libssl.so;/usr/lib/aarch64-linux-gnu/libcrypto.so;cmnghttp2
-- Looking for idn2_lookup_ul in idn2;dl;/usr/lib/aarch64-linux-gnu/libssl.so;/usr/lib/aarch64-linux-gnu/libcrypto.so;cmnghttp2 - not found
-- Looking for dlopen in dl;/usr/lib/aarch64-linux-gnu/libssl.so;/usr/lib/aarch64-linux-gnu/libcrypto.so;cmnghttp2
-- Looking for dlopen in dl;/usr/lib/aarch64-linux-gnu/libssl.so;/usr/lib/aarch64-linux-gnu/libcrypto.so;cmnghttp2 - not found
-- Looking for include files stdio.h, inttypes.h
-- Looking for include files stdio.h, inttypes.h - found
-- Looking for 3 include files stdio.h, ..., sys/filio.h
-- Looking for 3 include files stdio.h, ..., sys/filio.h - not found
-- Looking for 3 include files stdio.h, ..., sys/ioctl.h
-- Looking for 3 include files stdio.h, ..., sys/ioctl.h - found
-- Looking for 4 include files stdio.h, ..., sys/param.h
-- Looking for 4 include files stdio.h, ..., sys/param.h - found
-- Looking for 5 include files stdio.h, ..., sys/poll.h
-- Looking for 5 include files stdio.h, ..., sys/poll.h - found
-- Looking for 6 include files stdio.h, ..., sys/resource.h
-- Looking for 6 include files stdio.h, ..., sys/resource.h - found
-- Looking for 7 include files stdio.h, ..., sys/select.h
-- Looking for 7 include files stdio.h, ..., sys/select.h - found
-- Looking for 8 include files stdio.h, ..., sys/socket.h
-- Looking for 8 include files stdio.h, ..., sys/socket.h - found
-- Looking for 9 include files stdio.h, ..., sys/sockio.h
-- Looking for 9 include files stdio.h, ..., sys/sockio.h - not found
-- Looking for 9 include files stdio.h, ..., sys/stat.h
-- Looking for 9 include files stdio.h, ..., sys/stat.h - found
-- Looking for 10 include files stdio.h, ..., sys/time.h
-- Looking for 10 include files stdio.h, ..., sys/time.h - found
-- Looking for 11 include files stdio.h, ..., sys/types.h
-- Looking for 11 include files stdio.h, ..., sys/types.h - found
-- Looking for 12 include files stdio.h, ..., sys/uio.h
-- Looking for 12 include files stdio.h, ..., sys/uio.h - found
-- Looking for 13 include files stdio.h, ..., sys/un.h
-- Looking for 13 include files stdio.h, ..., sys/un.h - found
-- Looking for 14 include files stdio.h, ..., sys/utime.h
-- Looking for 14 include files stdio.h, ..., sys/utime.h - not found
-- Looking for 14 include files stdio.h, ..., sys/xattr.h
-- Looking for 14 include files stdio.h, ..., sys/xattr.h - found
-- Looking for 15 include files stdio.h, ..., alloca.h
-- Looking for 15 include files stdio.h, ..., alloca.h - found
-- Looking for 16 include files stdio.h, ..., arpa/inet.h
-- Looking for 16 include files stdio.h, ..., arpa/inet.h - found
-- Looking for 17 include files stdio.h, ..., arpa/tftp.h
-- Looking for 17 include files stdio.h, ..., arpa/tftp.h - found
-- Looking for 19 include files stdio.h, ..., crypto.h
-- Looking for 19 include files stdio.h, ..., crypto.h - not found
-- Looking for 19 include files stdio.h, ..., err.h
-- Looking for 19 include files stdio.h, ..., err.h - found
-- Looking for 20 include files stdio.h, ..., errno.h
-- Looking for 20 include files stdio.h, ..., errno.h - found
-- Looking for 21 include files stdio.h, ..., fcntl.h
-- Looking for 21 include files stdio.h, ..., fcntl.h - found
-- Looking for 22 include files stdio.h, ..., idn2.h
-- Looking for 22 include files stdio.h, ..., idn2.h - not found
-- Looking for 22 include files stdio.h, ..., ifaddrs.h
-- Looking for 22 include files stdio.h, ..., ifaddrs.h - found
-- Looking for 23 include files stdio.h, ..., io.h
-- Looking for 23 include files stdio.h, ..., io.h - not found
-- Looking for 23 include files stdio.h, ..., krb.h
-- Looking for 23 include files stdio.h, ..., krb.h - not found
-- Looking for 23 include files stdio.h, ..., libgen.h
-- Looking for 23 include files stdio.h, ..., libgen.h - found
-- Looking for 25 include files stdio.h, ..., net/if.h
-- Looking for 25 include files stdio.h, ..., net/if.h - found
-- Looking for 26 include files stdio.h, ..., netdb.h
-- Looking for 26 include files stdio.h, ..., netdb.h - found
-- Looking for 27 include files stdio.h, ..., netinet/in.h
-- Looking for 27 include files stdio.h, ..., netinet/in.h - found
-- Looking for 28 include files stdio.h, ..., netinet/tcp.h
-- Looking for 28 include files stdio.h, ..., netinet/tcp.h - found
-- Looking for 29 include files stdio.h, ..., pem.h
-- Looking for 29 include files stdio.h, ..., pem.h - not found
-- Looking for 29 include files stdio.h, ..., poll.h
-- Looking for 29 include files stdio.h, ..., poll.h - found
-- Looking for 30 include files stdio.h, ..., pwd.h
-- Looking for 30 include files stdio.h, ..., pwd.h - found
-- Looking for 31 include files stdio.h, ..., rsa.h
-- Looking for 31 include files stdio.h, ..., rsa.h - not found
-- Looking for 31 include files stdio.h, ..., setjmp.h
-- Looking for 31 include files stdio.h, ..., setjmp.h - found
-- Looking for 32 include files stdio.h, ..., sgtty.h
-- Looking for 32 include files stdio.h, ..., sgtty.h - found
-- Looking for 33 include files stdio.h, ..., signal.h
-- Looking for 33 include files stdio.h, ..., signal.h - found
-- Looking for 34 include files stdio.h, ..., ssl.h
-- Looking for 34 include files stdio.h, ..., ssl.h - not found
-- Looking for 34 include files stdio.h, ..., stdbool.h
-- Looking for 34 include files stdio.h, ..., stdbool.h - found
-- Looking for 35 include files stdio.h, ..., stdint.h
-- Looking for 35 include files stdio.h, ..., stdint.h - found
-- Looking for 39 include files stdio.h, ..., strings.h
-- Looking for 39 include files stdio.h, ..., strings.h - found
-- Looking for 40 include files stdio.h, ..., stropts.h
-- Looking for 40 include files stdio.h, ..., stropts.h - found
-- Looking for 41 include files stdio.h, ..., termio.h
-- Looking for 41 include files stdio.h, ..., termio.h - found
-- Looking for 42 include files stdio.h, ..., termios.h
-- Looking for 42 include files stdio.h, ..., termios.h - found
-- Looking for 43 include files stdio.h, ..., time.h
-- Looking for 43 include files stdio.h, ..., time.h - found
-- Looking for 44 include files stdio.h, ..., unistd.h
-- Looking for 44 include files stdio.h, ..., unistd.h - found
-- Looking for 45 include files stdio.h, ..., utime.h
-- Looking for 45 include files stdio.h, ..., utime.h - found
-- Looking for 46 include files stdio.h, ..., x509.h
-- Looking for 46 include files stdio.h, ..., x509.h - not found
-- Looking for 46 include files stdio.h, ..., process.h
-- Looking for 46 include files stdio.h, ..., process.h - not found
-- Looking for 47 include files stdio.h, ..., dlfcn.h
-- Looking for 47 include files stdio.h, ..., dlfcn.h - found
-- Looking for 48 include files stdio.h, ..., malloc.h
-- Looking for 48 include files stdio.h, ..., malloc.h - found
-- Looking for 49 include files stdio.h, ..., memory.h
-- Looking for 49 include files stdio.h, ..., memory.h - found
-- Looking for 50 include files stdio.h, ..., netinet/if_ether.h
-- Looking for 50 include files stdio.h, ..., netinet/if_ether.h - found
-- Looking for 52 include files stdio.h, ..., sockio.h
-- Looking for 52 include files stdio.h, ..., sockio.h - not found
-- Looking for 52 include files stdio.h, ..., sys/utsname.h
-- Looking for 52 include files stdio.h, ..., sys/utsname.h - found
-- Check size of size_t
-- Check size of size_t - done
-- Check size of ssize_t
-- Check size of ssize_t - done
-- Check size of time_t
-- Check size of time_t - done
-- Looking for basename
-- Looking for basename - found
-- Looking for socket
-- Looking for socket - found
-- Looking for select
-- Looking for select - found
-- Looking for poll
-- Looking for poll - found
-- Looking for strstr
-- Looking for strstr - found
-- Looking for strtok_r
-- Looking for strtok_r - found
-- Looking for uname
-- Looking for uname - found
-- Looking for strcasecmp
-- Looking for strcasecmp - found
-- Looking for stricmp
-- Looking for stricmp - not found
-- Looking for strcmpi
-- Looking for strcmpi - not found
-- Looking for strncmpi
-- Looking for strncmpi - not found
-- Looking for alarm
-- Looking for alarm - found
-- Looking for gethostbyaddr
-- Looking for gethostbyaddr - found
-- Looking for gethostbyaddr_r
-- Looking for gethostbyaddr_r - found
-- Looking for gettimeofday
-- Looking for gettimeofday - found
-- Looking for inet_addr
-- Looking for inet_addr - found
-- Looking for inet_ntoa
-- Looking for inet_ntoa - found
-- Looking for inet_ntoa_r
-- Looking for inet_ntoa_r - not found
-- Looking for tcsetattr
-- Looking for tcsetattr - found
-- Looking for tcgetattr
-- Looking for tcgetattr - found
-- Looking for perror
-- Looking for perror - found
-- Looking for closesocket
-- Looking for closesocket - not found
-- Looking for setvbuf
-- Looking for setvbuf - found
-- Looking for sigsetjmp
-- Looking for sigsetjmp - found
-- Looking for getpass_r
-- Looking for getpass_r - not found
-- Looking for strlcat
-- Looking for strlcat - not found
-- Looking for getpwuid
-- Looking for getpwuid - found
-- Looking for getpwuid_r
-- Looking for getpwuid_r - found
-- Looking for geteuid
-- Looking for geteuid - found
-- Looking for usleep
-- Looking for usleep - found
-- Looking for utime
-- Looking for utime - found
-- Looking for gmtime_r
-- Looking for gmtime_r - found
-- Looking for localtime_r
-- Looking for localtime_r - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for gethostbyname_r
-- Looking for gethostbyname_r - found
-- Looking for signal
-- Looking for signal - found
-- Looking for SIGALRM
-- Looking for SIGALRM - found
-- Looking for strtoll
-- Looking for strtoll - found
-- Looking for _strtoi64
-- Looking for _strtoi64 - not found
-- Looking for strerror_r
-- Looking for strerror_r - found
-- Looking for siginterrupt
-- Looking for siginterrupt - found
-- Looking for fork
-- Looking for fork - found
-- Looking for getaddrinfo
-- Looking for getaddrinfo - found
-- Looking for freeaddrinfo
-- Looking for freeaddrinfo - found
-- Looking for freeifaddrs
-- Looking for freeifaddrs - found
-- Looking for pipe
-- Looking for pipe - found
-- Looking for ftruncate
-- Looking for ftruncate - found
-- Looking for getprotobyname
-- Looking for getprotobyname - found
-- Looking for getpeername
-- Looking for getpeername - found
-- Looking for getsockname
-- Looking for getsockname - found
-- Looking for if_nametoindex
-- Looking for if_nametoindex - found
-- Looking for getrlimit
-- Looking for getrlimit - found
-- Looking for setmode
-- Looking for setmode - not found
-- Looking for setrlimit
-- Looking for setrlimit - found
-- Looking for fcntl
-- Looking for fcntl - found
-- Looking for ioctl
-- Looking for ioctl - found
-- Looking for setsockopt
-- Looking for setsockopt - found
-- Looking for mach_absolute_time
-- Looking for mach_absolute_time - not found
-- Looking for inet_pton
-- Looking for inet_pton - found
-- Looking for fsetxattr
-- Looking for fsetxattr - found
-- Performing Curl Test HAVE_FSETXATTR_5
-- Performing Curl Test HAVE_FSETXATTR_5 - Success
-- Performing Curl Test HAVE_FSETXATTR_6
-- Performing Curl Test HAVE_FSETXATTR_6 - Failed
-- Looking for sigaction
-- Looking for sigaction - found
-- Performing Curl Test HAVE_FCNTL_O_NONBLOCK
-- Performing Curl Test HAVE_FCNTL_O_NONBLOCK - Success
-- Performing Curl Test HAVE_IOCTLSOCKET
-- Performing Curl Test HAVE_IOCTLSOCKET - Failed
-- Performing Curl Test HAVE_IOCTLSOCKET_CAMEL
-- Performing Curl Test HAVE_IOCTLSOCKET_CAMEL - Failed
-- Performing Curl Test HAVE_IOCTLSOCKET_CAMEL_FIONBIO
-- Performing Curl Test HAVE_IOCTLSOCKET_CAMEL_FIONBIO - Failed
-- Performing Curl Test HAVE_IOCTLSOCKET_FIONBIO
-- Performing Curl Test HAVE_IOCTLSOCKET_FIONBIO - Failed
-- Performing Curl Test HAVE_IOCTL_FIONBIO
-- Performing Curl Test HAVE_IOCTL_FIONBIO - Success
-- Performing Curl Test HAVE_IOCTL_SIOCGIFADDR
-- Performing Curl Test HAVE_IOCTL_SIOCGIFADDR - Success
-- Performing Curl Test HAVE_SETSOCKOPT_SO_NONBLOCK
-- Performing Curl Test HAVE_SETSOCKOPT_SO_NONBLOCK - Failed
-- Performing Curl Test TIME_WITH_SYS_TIME
-- Performing Curl Test TIME_WITH_SYS_TIME - Success
-- Performing Curl Test HAVE_O_NONBLOCK
-- Performing Curl Test HAVE_O_NONBLOCK - Failed
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_5
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_5 - Failed
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_7
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_7 - Failed
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_8
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_8 - Success
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_5_REENTRANT
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_5_REENTRANT - Failed
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_7_REENTRANT
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_7_REENTRANT - Failed
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_8_REENTRANT
-- Performing Curl Test HAVE_GETHOSTBYADDR_R_8_REENTRANT - Success
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_3
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_3 - Failed
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_5
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_5 - Failed
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_6
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_6 - Success
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_3_REENTRANT
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_3_REENTRANT - Failed
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_5_REENTRANT
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_5_REENTRANT - Failed
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_6_REENTRANT
-- Performing Curl Test HAVE_GETHOSTBYNAME_R_6_REENTRANT - Success
-- Performing Curl Test HAVE_IN_ADDR_T
-- Performing Curl Test HAVE_IN_ADDR_T - Success
-- Performing Curl Test HAVE_BOOL_T
-- Performing Curl Test HAVE_BOOL_T - Success
-- Performing Curl Test STDC_HEADERS
-- Performing Curl Test STDC_HEADERS - Success
-- Performing Curl Test RETSIGTYPE_TEST
-- Performing Curl Test RETSIGTYPE_TEST - Success
-- Performing Curl Test HAVE_INET_NTOA_R_DECL
-- Performing Curl Test HAVE_INET_NTOA_R_DECL - Failed
-- Performing Curl Test HAVE_INET_NTOA_R_DECL_REENTRANT
-- Performing Curl Test HAVE_INET_NTOA_R_DECL_REENTRANT - Failed
-- Performing Curl Test HAVE_FILE_OFFSET_BITS
-- Performing Curl Test HAVE_FILE_OFFSET_BITS - Success
-- Performing Curl Test HAVE_VARIADIC_MACROS_C99
-- Performing Curl Test HAVE_VARIADIC_MACROS_C99 - Success
-- Performing Curl Test HAVE_VARIADIC_MACROS_GCC
-- Performing Curl Test HAVE_VARIADIC_MACROS_GCC - Success
-- Check size of off_t
-- Check size of off_t - done
-- Check size of curl_off_t
-- Check size of curl_off_t - done
-- Performing Curl Test HAVE_GLIBC_STRERROR_R
-- Performing Curl Test HAVE_GLIBC_STRERROR_R - Failed
-- Performing Curl Test HAVE_POSIX_STRERROR_R
-- Performing Curl Test HAVE_POSIX_STRERROR_R - Success
-- Performing Curl Test HAVE_CLOCK_GETTIME_MONOTONIC
-- Performing Curl Test HAVE_CLOCK_GETTIME_MONOTONIC - Success
-- Performing Curl Test HAVE_BUILTIN_AVAILABLE
-- Performing Curl Test HAVE_BUILTIN_AVAILABLE - Failed
-- Performing Test HAVE_MSG_NOSIGNAL
-- Performing Test HAVE_MSG_NOSIGNAL - Success
-- Performing Test HAVE_STRUCT_TIMEVAL
-- Performing Test HAVE_STRUCT_TIMEVAL - Success
-- Check size of sig_atomic_t
-- Check size of sig_atomic_t - done
-- Performing Test HAVE_SIG_ATOMIC_T_NOT_VOLATILE
-- Performing Test HAVE_SIG_ATOMIC_T_NOT_VOLATILE - Success
-- Check size of struct sockaddr_storage
-- Check size of struct sockaddr_storage - done
-- Performing Test HAVE_POLL_FINE
-- Performing Test HAVE_POLL_FINE - Success
-- Looking for getpagesize
-- Looking for getpagesize - found
-- Looking for mmap
-- Looking for mmap - found
-- Looking for getrandom
-- Looking for getrandom - found
-- Looking for arc4random_buf
-- Looking for arc4random_buf - not found
-- Looking for arc4random
-- Looking for arc4random - not found
-- Check if the system is big endian
-- Searching 16 bit integer
-- Searching 16 bit integer - Using unsigned short
-- Check if the system is big endian - little endian
-- Performing Test HAVE_SYSCALL_GETRANDOM
-- Performing Test HAVE_SYSCALL_GETRANDOM - Success
-- Looking for byteswap.h
-- Looking for byteswap.h - found
-- Looking for limits.h
-- Looking for limits.h - found
-- Looking for sys/sysctl.h
-- Looking for sys/sysctl.h - found
-- Performing Test HAVE_BSWAP_16
-- Performing Test HAVE_BSWAP_16 - Success
-- Performing Test HAVE_BSWAP_32
-- Performing Test HAVE_BSWAP_32 - Success
-- Performing Test HAVE_BSWAP_64
-- Performing Test HAVE_BSWAP_64 - Success
-- Found ZLIB: cmzlib  
-- Found BZip2: cmbzip2 (found version "1.0.8") 
-- Found LibLZMA: cmliblzma (found version "5.2.4") 
-- Performing Test HAVE_DIRENT_H
-- Performing Test HAVE_DIRENT_H - Success
-- Looking for 3 include files sys/types.h, ..., copyfile.h
-- Looking for 3 include files sys/types.h, ..., copyfile.h - not found
-- Looking for 3 include files sys/types.h, ..., direct.h
-- Looking for 3 include files sys/types.h, ..., direct.h - not found
-- Looking for 5 include files sys/types.h, ..., ext2fs/ext2_fs.h
-- Looking for 5 include files sys/types.h, ..., ext2fs/ext2_fs.h - not found
-- Performing Test HAVE_WORKING_EXT2_IOC_GETFLAGS
-- Performing Test HAVE_WORKING_EXT2_IOC_GETFLAGS - Failed
-- Looking for 6 include files sys/types.h, ..., grp.h
-- Looking for 6 include files sys/types.h, ..., grp.h - found
-- Looking for 7 include files sys/types.h, ..., langinfo.h
-- Looking for 7 include files sys/types.h, ..., langinfo.h - found
-- Looking for 9 include files sys/types.h, ..., linux/types.h
-- Looking for 9 include files sys/types.h, ..., linux/types.h - found
-- Looking for 10 include files sys/types.h, ..., linux/fiemap.h
-- Looking for 10 include files sys/types.h, ..., linux/fiemap.h - found
-- Looking for 11 include files sys/types.h, ..., linux/fs.h
-- Looking for 11 include files sys/types.h, ..., linux/fs.h - found
-- Performing Test HAVE_WORKING_FS_IOC_GETFLAGS
-- Performing Test HAVE_WORKING_FS_IOC_GETFLAGS - Success
-- Looking for 12 include files sys/types.h, ..., linux/magic.h
-- Looking for 12 include files sys/types.h, ..., linux/magic.h - found
-- Looking for 14 include files sys/types.h, ..., membership.h
-- Looking for 14 include files sys/types.h, ..., membership.h - not found
-- Looking for 15 include files sys/types.h, ..., paths.h
-- Looking for 15 include files sys/types.h, ..., paths.h - found
-- Looking for 17 include files sys/types.h, ..., pthread.h
-- Looking for 17 include files sys/types.h, ..., pthread.h - found
-- Looking for 19 include files sys/types.h, ..., readpassphrase.h
-- Looking for 19 include files sys/types.h, ..., readpassphrase.h - not found
-- Looking for 19 include files sys/types.h, ..., regex.h
-- Looking for 19 include files sys/types.h, ..., regex.h - found
-- Looking for 21 include files sys/types.h, ..., spawn.h
-- Looking for 21 include files sys/types.h, ..., spawn.h - found
-- Looking for 22 include files sys/types.h, ..., stdarg.h
-- Looking for 22 include files sys/types.h, ..., stdarg.h - found
-- Looking for 26 include files sys/types.h, ..., sys/acl.h
-- Looking for 26 include files sys/types.h, ..., sys/acl.h - not found
-- Looking for 26 include files sys/types.h, ..., sys/cdefs.h
-- Looking for 26 include files sys/types.h, ..., sys/cdefs.h - found
-- Looking for 27 include files sys/types.h, ..., sys/extattr.h
-- Looking for 27 include files sys/types.h, ..., sys/extattr.h - not found
-- Looking for 28 include files sys/types.h, ..., sys/mkdev.h
-- Looking for 28 include files sys/types.h, ..., sys/mkdev.h - not found
-- Looking for 28 include files sys/types.h, ..., sys/mount.h
-- Looking for 28 include files sys/types.h, ..., sys/mount.h - not found
-- Looking for 30 include files sys/types.h, ..., sys/richacl.h
-- Looking for 30 include files sys/types.h, ..., sys/richacl.h - not found
-- Looking for 32 include files sys/types.h, ..., sys/statfs.h
-- Looking for 32 include files sys/types.h, ..., sys/statfs.h - found
-- Looking for 33 include files sys/types.h, ..., sys/statvfs.h
-- Looking for 33 include files sys/types.h, ..., sys/statvfs.h - found
-- Looking for 34 include files sys/types.h, ..., sys/sysmacros.h
-- Looking for 34 include files sys/types.h, ..., sys/sysmacros.h - found
-- Looking for 37 include files sys/types.h, ..., sys/vfs.h
-- Looking for 37 include files sys/types.h, ..., sys/vfs.h - found
-- Looking for 38 include files sys/types.h, ..., sys/wait.h
-- Looking for 38 include files sys/types.h, ..., sys/wait.h - found
-- Looking for 44 include files sys/types.h, ..., wctype.h
-- Looking for 44 include files sys/types.h, ..., wctype.h - found
-- Looking for 45 include files sys/types.h, ..., windows.h
-- Looking for 45 include files sys/types.h, ..., windows.h - not found
-- Looking for 45 include files sys/types.h, ..., wincrypt.h
-- Looking for 45 include files sys/types.h, ..., wincrypt.h - not found
-- Looking for 45 include files sys/types.h, ..., winioctl.h
-- Looking for 45 include files sys/types.h, ..., winioctl.h - not found
-- Performing Test SAFE_TO_DEFINE_EXTENSIONS
-- Performing Test SAFE_TO_DEFINE_EXTENSIONS - Success
-- Looking for chown
-- Looking for chown - found
-- Looking for chroot
-- Looking for chroot - found
-- Looking for ctime_r
-- Looking for ctime_r - found
-- Looking for fchdir
-- Looking for fchdir - found
-- Looking for fchmod
-- Looking for fchmod - found
-- Looking for fchown
-- Looking for fchown - found
-- Looking for fdopendir
-- Looking for fdopendir - found
-- Looking for fstat
-- Looking for fstat - found
-- Looking for fstatat
-- Looking for fstatat - found
-- Looking for fstatfs
-- Looking for fstatfs - found
-- Looking for fstatvfs
-- Looking for fstatvfs - found
-- Looking for futimens
-- Looking for futimens - found
-- Looking for futimes
-- Looking for futimes - found
-- Looking for futimesat
-- Looking for futimesat - found
-- Looking for getgrgid_r
-- Looking for getgrgid_r - found
-- Looking for getgrnam_r
-- Looking for getgrnam_r - found
-- Looking for getpwnam_r
-- Looking for getpwnam_r - found
-- Looking for getpid
-- Looking for getpid - found
-- Looking for getvfsbyname
-- Looking for getvfsbyname - not found
-- Looking for lchflags
-- Looking for lchflags - not found
-- Looking for lchown
-- Looking for lchown - found
-- Looking for link
-- Looking for link - found
-- Looking for lstat
-- Looking for lstat - found
-- Looking for lutimes
-- Looking for lutimes - found
-- Looking for mbrtowc
-- Looking for mbrtowc - found
-- Looking for mkdir
-- Looking for mkdir - found
-- Looking for mkfifo
-- Looking for mkfifo - found
-- Looking for mknod
-- Looking for mknod - found
-- Looking for mkstemp
-- Looking for mkstemp - found
-- Looking for nl_langinfo
-- Looking for nl_langinfo - found
-- Looking for openat
-- Looking for openat - found
-- Looking for posix_spawnp
-- Looking for posix_spawnp - found
-- Looking for readlink
-- Looking for readlink - found
-- Looking for readpassphrase
-- Looking for readpassphrase - not found
-- Looking for setenv
-- Looking for setenv - found
-- Looking for statfs
-- Looking for statfs - found
-- Looking for statvfs
-- Looking for statvfs - found
-- Looking for strerror
-- Looking for strerror - found
-- Looking for strncpy_s
-- Looking for strncpy_s - not found
-- Looking for symlink
-- Looking for symlink - found
-- Looking for timegm
-- Looking for timegm - found
-- Looking for tzset
-- Looking for tzset - found
-- Looking for unlinkat
-- Looking for unlinkat - found
-- Looking for utimes
-- Looking for utimes - found
-- Looking for utimensat
-- Looking for utimensat - found
-- Looking for vfork
-- Looking for vfork - found
-- Looking for wcrtomb
-- Looking for wcrtomb - found
-- Looking for wcscmp
-- Looking for wcscmp - found
-- Looking for wcscpy
-- Looking for wcscpy - found
-- Looking for wcslen
-- Looking for wcslen - found
-- Looking for wctomb
-- Looking for wctomb - found
-- Looking for _ctime64_s
-- Looking for _ctime64_s - not found
-- Looking for _fseeki64
-- Looking for _fseeki64 - not found
-- Looking for _get_timezone
-- Looking for _get_timezone - not found
-- Looking for _gmtime64_s
-- Looking for _gmtime64_s - not found
-- Looking for _localtime64_s
-- Looking for _localtime64_s - not found
-- Looking for _mkgmtime64
-- Looking for _mkgmtime64 - not found
-- Looking for cygwin_conv_path
-- Looking for cygwin_conv_path - not found
-- Looking for fseeko
-- Looking for fseeko - found
-- Looking for vprintf
-- Looking for vprintf - found
-- Looking for wmemcmp
-- Looking for wmemcmp - found
-- Looking for wmemcpy
-- Looking for wmemcpy - found
-- Looking for wmemmove
-- Looking for wmemmove - found
-- Performing Test HAVE_STRUCT_VFSCONF
-- Performing Test HAVE_STRUCT_VFSCONF - Failed
-- Performing Test HAVE_STRUCT_XVFSCONF
-- Performing Test HAVE_STRUCT_XVFSCONF - Failed
-- Performing Test HAVE_READDIR_R
-- Performing Test HAVE_READDIR_R - Success
-- Performing Test HAVE_DIRFD
-- Performing Test HAVE_DIRFD - Success
-- Performing Test HAVE_READLINKAT
-- Performing Test HAVE_READLINKAT - Success
-- Performing Test MAJOR_IN_MKDEV
-- Performing Test MAJOR_IN_MKDEV - Failed
-- Performing Test MAJOR_IN_SYSMACROS
-- Performing Test MAJOR_IN_SYSMACROS - Success
-- Performing Test HAVE_LZMA_STREAM_ENCODER_MT
-- Performing Test HAVE_LZMA_STREAM_ENCODER_MT - Failed
-- Looking for EFTYPE
-- Looking for EFTYPE - not found
-- Looking for EILSEQ
-- Looking for EILSEQ - found
-- Looking for D_MD_ORDER
-- Looking for D_MD_ORDER - not found
-- Performing Test HAVE_STRUCT_TM_TM_GMTOFF
-- Performing Test HAVE_STRUCT_TM_TM_GMTOFF - Success
-- Performing Test HAVE_STRUCT_TM___TM_GMTOFF
-- Performing Test HAVE_STRUCT_TM___TM_GMTOFF - Failed
-- Performing Test HAVE_STRUCT_STATFS_F_NAMEMAX
-- Performing Test HAVE_STRUCT_STATFS_F_NAMEMAX - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_BIRTHTIME
-- Performing Test HAVE_STRUCT_STAT_ST_BIRTHTIME - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_BIRTHTIMESPEC_TV_NSEC
-- Performing Test HAVE_STRUCT_STAT_ST_BIRTHTIMESPEC_TV_NSEC - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_MTIMESPEC_TV_NSEC
-- Performing Test HAVE_STRUCT_STAT_ST_MTIMESPEC_TV_NSEC - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_MTIM_TV_NSEC
-- Performing Test HAVE_STRUCT_STAT_ST_MTIM_TV_NSEC - Success
-- Performing Test HAVE_STRUCT_STAT_ST_MTIME_N
-- Performing Test HAVE_STRUCT_STAT_ST_MTIME_N - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_UMTIME
-- Performing Test HAVE_STRUCT_STAT_ST_UMTIME - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_MTIME_USEC
-- Performing Test HAVE_STRUCT_STAT_ST_MTIME_USEC - Failed
-- Performing Test HAVE_STRUCT_STAT_ST_BLKSIZE
-- Performing Test HAVE_STRUCT_STAT_ST_BLKSIZE - Success
-- Performing Test HAVE_STRUCT_STAT_ST_FLAGS
-- Performing Test HAVE_STRUCT_STAT_ST_FLAGS - Failed
-- Performing Test HAVE_STRUCT_STATVFS_F_IOSIZE
-- Performing Test HAVE_STRUCT_STATVFS_F_IOSIZE - Failed
-- Check size of dev_t
-- Check size of dev_t - done
-- Check size of gid_t
-- Check size of gid_t - done
-- Check size of id_t
-- Check size of id_t - done
-- Check size of mode_t
-- Check size of mode_t - done
-- Check size of off_t
-- Check size of off_t - done
-- Check size of size_t
-- Check size of size_t - done
-- Check size of ssize_t
-- Check size of ssize_t - done
-- Check size of uid_t
-- Check size of uid_t - done
-- Check size of pid_t
-- Check size of pid_t - done
-- Check size of wchar_t
-- Check size of wchar_t - done
-- Checking _FILE_OFFSET_BITS for large files
-- Checking _FILE_OFFSET_BITS for large files - not needed
-- Checking support for ARCHIVE_CRYPTO_MD5_LIBC
-- Checking support for ARCHIVE_CRYPTO_MD5_LIBC -- not found
-- Checking support for ARCHIVE_CRYPTO_RMD160_LIBC
-- Checking support for ARCHIVE_CRYPTO_RMD160_LIBC -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA1_LIBC
-- Checking support for ARCHIVE_CRYPTO_SHA1_LIBC -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBC
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBC -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBC
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBC -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBC
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBC -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBC2
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBC2 -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBC2
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBC2 -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBC2
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBC2 -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBC3
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBC3 -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBC3
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBC3 -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBC3
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBC3 -- not found
-- Checking support for ARCHIVE_CRYPTO_MD5_LIBSYSTEM
-- Checking support for ARCHIVE_CRYPTO_MD5_LIBSYSTEM -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA1_LIBSYSTEM
-- Checking support for ARCHIVE_CRYPTO_SHA1_LIBSYSTEM -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBSYSTEM
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBSYSTEM -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBSYSTEM
-- Checking support for ARCHIVE_CRYPTO_SHA384_LIBSYSTEM -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBSYSTEM
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBSYSTEM -- not found
-- Checking support for ARCHIVE_CRYPTO_MD5_OPENSSL
-- Checking support for ARCHIVE_CRYPTO_MD5_OPENSSL -- not found
-- Checking support for ARCHIVE_CRYPTO_RMD160_OPENSSL
-- Checking support for ARCHIVE_CRYPTO_RMD160_OPENSSL -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA1_OPENSSL
-- Checking support for ARCHIVE_CRYPTO_SHA1_OPENSSL -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA256_OPENSSL
-- Checking support for ARCHIVE_CRYPTO_SHA256_OPENSSL -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA384_OPENSSL
-- Checking support for ARCHIVE_CRYPTO_SHA384_OPENSSL -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA512_OPENSSL
-- Checking support for ARCHIVE_CRYPTO_SHA512_OPENSSL -- not found
-- Checking support for ARCHIVE_CRYPTO_MD5_LIBMD
-- Checking support for ARCHIVE_CRYPTO_MD5_LIBMD -- not found
-- Checking support for ARCHIVE_CRYPTO_RMD160_LIBMD
-- Checking support for ARCHIVE_CRYPTO_RMD160_LIBMD -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA1_LIBMD
-- Checking support for ARCHIVE_CRYPTO_SHA1_LIBMD -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBMD
-- Checking support for ARCHIVE_CRYPTO_SHA256_LIBMD -- not found
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBMD
-- Checking support for ARCHIVE_CRYPTO_SHA512_LIBMD -- not found
-- Checking for curses support
-- Checking for curses support - Failed
-- Looking for elf.h
-- Looking for elf.h - found
-- Looking for a Fortran compiler
-- Looking for a Fortran compiler - NOTFOUND
qmake: could not exec '/usr/lib/aarch64-linux-gnu/qt4/bin/qmake': No such file or directory
qmake: could not exec '/usr/lib/aarch64-linux-gnu/qt4/bin/qmake': No such file or directory
-- Performing Test run_pic_test
-- Performing Test run_pic_test - Success
-- Performing Test run_inlines_hidden_test
-- Performing Test run_inlines_hidden_test - Success
-- Configuring done
-- Generating done
-- Build files have been written to: /home/user/temp/cmake-3.18.1
---------------------------------------------
CMake has bootstrapped.  Now run make. 
```
**출력 결과**
```bash
[  4%] Building C object Utilities/cmzlib/CMakeFiles/cmzlib.dir/inflate.c.o
[  4%] Building C object Utilities/cmzlib/CMakeFiles/cmzlib.dir/inftrees.c.o
[  4%] Building CXX object Source/kwsys/CMakeFiles/cmsys.dir/RegularExpression.cxx.o
[  4%] Building C object Utilities/cmzlib/CMakeFiles/cmzlib.dir/trees.c.o
[  4%] Building C object Utilities/cmzlib/CMakeFiles/cmzlib.dir/uncompr.c.o
[  4%] Building C object Utilities/cmzlib/CMakeFiles/cmzlib.dir/zutil.c.o
Scanning dependencies of target cmnghttp2
[  4%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_buf.c.o
[  4%] Linking C static library libcmzlib.a
[  4%] Built target cmzlib
[  4%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_callbacks.c.o
[  4%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_debug.c.o
[  4%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_frame.c.o
[  4%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_hd.c.o
[  4%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_hd_huffman.c.o
[  5%] Building CXX object Source/kwsys/CMakeFiles/cmsys.dir/SystemTools.cxx.o
[  5%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_hd_huffman_data.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_helper.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_http.c.o
[  6%] Building CXX object Source/kwsys/CMakeFiles/cmsys.dir/CommandLineArguments.cxx.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_map.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_mem.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_npn.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_option.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_outbound_item.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_pq.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_priority_spec.c.o
[  6%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_queue.c.o
[  7%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_rcbuf.c.o
[  7%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_session.c.o
[  7%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_stream.c.o
[  7%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_submit.c.o
[  7%] Building C object Utilities/cmnghttp2/CMakeFiles/cmnghttp2.dir/lib/nghttp2_version.c.o
Scanning dependencies of target cmexpat
[  7%] Building C object Utilities/cmexpat/CMakeFiles/cmexpat.dir/lib/xmlparse.c.o
[  7%] Building C object Utilities/cmexpat/CMakeFiles/cmexpat.dir/lib/xmlrole.c.o
[  7%] Linking C static library libcmnghttp2.a
[  7%] Built target cmnghttp2
[  7%] Building C object Utilities/cmexpat/CMakeFiles/cmexpat.dir/lib/xmltok.c.o
Scanning dependencies of target cmbzip2
[  8%] Building C object Utilities/cmbzip2/CMakeFiles/cmbzip2.dir/blocksort.c.o
[  8%] Building CXX object Source/kwsys/CMakeFiles/cmsys.dir/FStream.cxx.o
[  8%] Building C object Utilities/cmbzip2/CMakeFiles/cmbzip2.dir/huffman.c.o
[  8%] Building CXX object Source/kwsys/CMakeFiles/cmsys.dir/SystemInformation.cxx.o
[  8%] Building C object Utilities/cmbzip2/CMakeFiles/cmbzip2.dir/crctable.c.o
[  8%] Building C object Utilities/cmbzip2/CMakeFiles/cmbzip2.dir/randtable.c.o
[  9%] Building C object Utilities/cmexpat/CMakeFiles/cmexpat.dir/lib/xmltok_impl.c.o
[  9%] Building C object Utilities/cmbzip2/CMakeFiles/cmbzip2.dir/compress.c.o
[  9%] Building C object Utilities/cmexpat/CMakeFiles/cmexpat.dir/lib/xmltok_ns.c.o
Scanning dependencies of target cmzstd
[  9%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/common/entropy_common.c.o
[  9%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/common/error_private.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/common/fse_decompress.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/common/pool.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/common/threading.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/common/xxhash.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/common/zstd_common.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/fse_compress.c.o
[ 10%] Linking C static library libcmexpat.a
[ 10%] Built target cmexpat
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/hist.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/huf_compress.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/zstd_compress.c.o
[ 10%] Building C object Utilities/cmbzip2/CMakeFiles/cmbzip2.dir/decompress.c.o
[ 10%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/zstd_double_fast.c.o
[ 10%] Linking CXX static library libcmsys.a
[ 10%] Built target cmsys
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/zstd_fast.c.o
[ 11%] Building C object Utilities/cmbzip2/CMakeFiles/cmbzip2.dir/bzlib.c.o
[ 11%] Linking C static library libcmbzip2.a
[ 11%] Built target cmbzip2
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/zstd_lazy.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/zstd_ldm.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/zstdmt_compress.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/compress/zstd_opt.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/decompress/huf_decompress.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/decompress/zstd_ddict.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/decompress/zstd_decompress_block.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/decompress/zstd_decompress.c.o
[ 11%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/deprecated/zbuff_common.c.o
[ 12%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/deprecated/zbuff_compress.c.o
[ 12%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/deprecated/zbuff_decompress.c.o
[ 12%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/dictBuilder/cover.c.o
[ 12%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/dictBuilder/divsufsort.c.o
[ 12%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/dictBuilder/fastcover.c.o
[ 12%] Building C object Utilities/cmzstd/CMakeFiles/cmzstd.dir/lib/dictBuilder/zdict.c.o
Scanning dependencies of target cmliblzma
[ 12%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/check/check.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/check/crc32_fast.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/check/crc32_table.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/check/crc64_fast.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/check/crc64_table.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/check/sha256.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/alone_decoder.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/alone_encoder.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/auto_decoder.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/block_buffer_decoder.c.o
[ 13%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/block_buffer_encoder.c.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/block_decoder.c.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/block_encoder.c.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/block_header_decoder.c.o
Scanning dependencies of target cmjsoncpp
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/block_header_encoder.c.o
[ 14%] Building CXX object Utilities/cmjsoncpp/CMakeFiles/cmjsoncpp.dir/src/lib_json/json_reader.cpp.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/block_util.c.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/common.c.o
[ 14%] Building CXX object Utilities/cmjsoncpp/CMakeFiles/cmjsoncpp.dir/src/lib_json/json_value.cpp.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/easy_buffer_encoder.c.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/easy_decoder_memusage.c.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/easy_encoder.c.o
[ 14%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/easy_encoder_memusage.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/easy_preset.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/filter_buffer_decoder.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/filter_buffer_encoder.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/filter_common.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/filter_decoder.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/filter_encoder.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/filter_flags_decoder.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/filter_flags_encoder.c.o
[ 15%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/index.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/index_decoder.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/index_encoder.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/index_hash.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/stream_buffer_decoder.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/stream_buffer_encoder.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/stream_decoder.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/stream_encoder.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/stream_flags_common.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/stream_flags_decoder.c.o
[ 16%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/stream_flags_encoder.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/vli_decoder.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/vli_encoder.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/common/vli_size.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/delta/delta_common.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/delta/delta_decoder.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/delta/delta_encoder.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lz/lz_decoder.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lz/lz_encoder.c.o
[ 17%] Building CXX object Utilities/cmjsoncpp/CMakeFiles/cmjsoncpp.dir/src/lib_json/json_writer.cpp.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lz/lz_encoder_mf.c.o
[ 17%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/fastpos_table.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/lzma2_decoder.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/lzma2_encoder.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/lzma_decoder.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/lzma_encoder.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/lzma_encoder_optimum_fast.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/lzma_encoder_optimum_normal.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/lzma/lzma_encoder_presets.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/rangecoder/price_table.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/arm.c.o
[ 18%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/armthumb.c.o
[ 19%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/ia64.c.o
[ 19%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/powerpc.c.o
[ 19%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/simple_coder.c.o
[ 19%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/simple_decoder.c.o
[ 19%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/simple_encoder.c.o
[ 19%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/sparc.c.o
[ 19%] Building C object Utilities/cmliblzma/CMakeFiles/cmliblzma.dir/liblzma/simple/x86.c.o
Scanning dependencies of target cmlibuv
[ 19%] Linking C static library libcmliblzma.a
[ 19%] Built target cmliblzma
Scanning dependencies of target testUVProcessChainHelper
[ 19%] Building CXX object Tests/CMakeLib/CMakeFiles/testUVProcessChainHelper.dir/testUVProcessChainHelper.cxx.o
[ 19%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/fs-poll.c.o
[ 19%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/idna.c.o
[ 20%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/inet.c.o
[ 20%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/strscpy.c.o
[ 20%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/threadpool.c.o
[ 20%] Linking CXX static library libcmjsoncpp.a
[ 20%] Built target cmjsoncpp
[ 20%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/timer.c.o
[ 20%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/uv-common.c.o
[ 21%] Linking CXX executable testUVProcessChainHelper
[ 21%] Linking C static library libcmzstd.a
[ 21%] Built target cmzstd
[ 21%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/uv-data-getter-setters.c.o
[ 21%] Built target testUVProcessChainHelper
Scanning dependencies of target testEncoding
[ 21%] Building CXX object Tests/CMakeLib/CMakeFiles/testEncoding.dir/testEncoding.cxx.o
[ 21%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/version.c.o
[ 21%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/async.c.o
[ 21%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/core.c.o
[ 22%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/dl.c.o
[ 22%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/fs.c.o
[ 22%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/getaddrinfo.c.o
[ 22%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/getnameinfo.c.o
[ 22%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/loop-watcher.c.o
[ 22%] Linking CXX executable testEncoding
Scanning dependencies of target pseudonl_purify
[ 22%] Building C object Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/ret0.c.o
[ 22%] Linking C executable purify
[ 22%] Built target testEncoding
[ 22%] Built target pseudonl_purify
Scanning dependencies of target pseudonl_valgrind
Scanning dependencies of target pseudonl_BC
[ 22%] Building C object Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_BC.dir/ret0.c.o
[ 22%] Building C object Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_valgrind.dir/ret0.c.o
[ 22%] Linking C executable BC
[ 22%] Linking C executable valgrind
[ 22%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/loop.c.o
[ 22%] Built target pseudonl_valgrind
[ 22%] Built target pseudonl_BC
Scanning dependencies of target pseudo_emulator
[ 22%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/pipe.c.o
[ 23%] Building C object Tests/RunCMake/CMakeFiles/pseudo_emulator.dir/pseudo_emulator.c.o
[ 23%] Linking C executable pseudo_emulator
[ 23%] Built target pseudo_emulator
Scanning dependencies of target pseudo_emulator_custom_command
[ 23%] Building C object Tests/RunCMake/CMakeFiles/pseudo_emulator_custom_command.dir/pseudo_emulator_custom_command.c.o
[ 23%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/poll.c.o
[ 23%] Linking C executable pseudo_emulator_custom_command
[ 23%] Built target pseudo_emulator_custom_command
[ 23%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/process.c.o
Scanning dependencies of target print_stdin
[ 23%] Building C object Tests/RunCMake/CMakeFiles/print_stdin.dir/print_stdin.c.o
[ 23%] Linking C executable print_stdin
[ 23%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/signal.c.o
[ 24%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/stream.c.o
[ 24%] Built target print_stdin
Scanning dependencies of target pseudo_iwyu
[ 24%] Building C object Tests/RunCMake/CMakeFiles/pseudo_iwyu.dir/pseudo_iwyu.c.o
[ 24%] Linking C executable pseudo_iwyu
[ 24%] Built target pseudo_iwyu
Scanning dependencies of target pseudo_cppcheck
[ 24%] Building C object Tests/RunCMake/CMakeFiles/pseudo_cppcheck.dir/pseudo_cppcheck.c.o
[ 24%] Linking C executable pseudo_cppcheck
[ 24%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/tcp.c.o
[ 24%] Built target pseudo_cppcheck
Scanning dependencies of target exit_code
[ 24%] Building C object Tests/RunCMake/CMakeFiles/exit_code.dir/exit_code.c.o
[ 24%] Linking C executable exit_code
[ 24%] Built target exit_code
Scanning dependencies of target color_warning
[ 24%] Building C object Tests/RunCMake/CMakeFiles/color_warning.dir/color_warning.c.o
[ 24%] Linking C executable color_warning
[ 24%] Built target color_warning
Scanning dependencies of target pseudo_tidy
[ 25%] Building C object Tests/RunCMake/CMakeFiles/pseudo_tidy.dir/pseudo_tidy.c.o
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/thread.c.o
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/tty.c.o
[ 25%] Linking C executable pseudo_tidy
Scanning dependencies of target pseudo_emulator_custom_command_arg
[ 25%] Building C object Tests/RunCMake/CMakeFiles/pseudo_emulator_custom_command_arg.dir/pseudo_emulator_custom_command_arg.c.o
[ 25%] Built target pseudo_tidy
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/udp.c.o
[ 25%] Linking C executable pseudo_emulator_custom_command_arg
[ 25%] Built target pseudo_emulator_custom_command_arg
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/linux-core.c.o
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/linux-inotify.c.o
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/linux-syscalls.c.o
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/procfs-exepath.c.o
[ 25%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/proctitle.c.o
Scanning dependencies of target pseudo_cpplint
[ 25%] Building C object Tests/RunCMake/CMakeFiles/pseudo_cpplint.dir/pseudo_cpplint.c.o
[ 26%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/sysinfo-loadavg.c.o
[ 26%] Building C object Utilities/cmlibuv/CMakeFiles/cmlibuv.dir/src/unix/sysinfo-memory.c.o
Scanning dependencies of target foo
[ 27%] Building CXX object Tests/FindPackageModeMakefileTest/CMakeFiles/foo.dir/foo.cpp.o
[ 27%] Linking C executable pseudo_cpplint
[ 27%] Linking CXX static library libfoo.a
[ 27%] Built target pseudo_cpplint
[ 27%] Built target foo
Scanning dependencies of target cmsysTestsCxx
Scanning dependencies of target cmsysTestDynload
Scanning dependencies of target testConsoleBufChild
[ 27%] Building C object Source/kwsys/CMakeFiles/cmsysTestDynload.dir/testDynload.c.o
[ 27%] Building CXX object Source/kwsys/CMakeFiles/testConsoleBufChild.dir/testConsoleBufChild.cxx.o
[ 27%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/cmsysTestsCxx.cxx.o
[ 27%] Linking C shared module libcmsysTestDynload.so
[ 27%] Linking C static library libcmlibuv.a
[ 27%] Built target cmsysTestDynload
[ 27%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testConfigure.cxx.o
[ 27%] Built target cmlibuv
[ 27%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testSystemTools.cxx.o
[ 27%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testCommandLineArguments.cxx.o
[ 28%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testCommandLineArguments1.cxx.o
[ 28%] Linking CXX executable testConsoleBufChild
[ 28%] Built target testConsoleBufChild
[ 28%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testDirectory.cxx.o
Scanning dependencies of target cmsysTestProcess
[ 28%] Building C object Source/kwsys/CMakeFiles/cmsysTestProcess.dir/testProcess.c.o
[ 28%] Linking C executable cmsysTestProcess
[ 28%] Built target cmsysTestProcess
[ 28%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testEncoding.cxx.o
[ 28%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testFStream.cxx.o
[ 28%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testConsoleBuf.cxx.o
[ 28%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testSystemInformation.cxx.o
[ 28%] Building CXX object Source/kwsys/CMakeFiles/cmsysTestsCxx.dir/testDynamicLoader.cxx.o
Scanning dependencies of target cmsysTestSharedForward
[ 29%] Building C object Source/kwsys/CMakeFiles/cmsysTestSharedForward.dir/testSharedForward.c.o
[ 29%] Linking C executable cmsysTestSharedForward
[ 29%] Built target cmsysTestSharedForward
Scanning dependencies of target cmsysTestsC
[ 29%] Building C object Source/kwsys/CMakeFiles/cmsysTestsC.dir/cmsysTestsC.c.o
[ 29%] Building C object Source/kwsys/CMakeFiles/cmsysTestsC.dir/testEncode.c.o
[ 29%] Building C object Source/kwsys/CMakeFiles/cmsysTestsC.dir/testTerminal.c.o
[ 29%] Linking C executable cmsysTestsC
[ 29%] Built target cmsysTestsC
Scanning dependencies of target cmcurl
Scanning dependencies of target cmlibarchive
[ 29%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_acl.c.o
[ 29%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_check_magic.c.o
[ 29%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_cmdline.c.o
[ 30%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_cryptor.c.o
[ 30%] Linking CXX executable cmsysTestsCxx
[ 30%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_digest.c.o
[ 30%] Built target cmsysTestsCxx
[ 30%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_entry.c.o
[ 30%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_entry_copy_stat.c.o
[ 30%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_entry_link_resolver.c.o
[ 30%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_entry_sparse.c.o
[ 30%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/altsvc.c.o
[ 30%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/amigaos.c.o
[ 30%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_entry_stat.c.o
[ 31%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/asyn-ares.c.o
[ 31%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_entry_strmode.c.o
[ 31%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/asyn-thread.c.o
[ 31%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_entry_xattr.c.o
[ 31%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/base64.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_getdate.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_hmac.c.o
[ 32%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/conncache.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_match.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_options.c.o
[ 32%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/connect.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_pack_dev.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_pathmatch.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_ppmd8.c.o
[ 32%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/content_encoding.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_ppmd7.c.o
[ 32%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/cookie.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_random.c.o
[ 32%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_rb.c.o
[ 33%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read.c.o
[ 33%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_add_passphrase.c.o
[ 33%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_append_filter.c.o
[ 33%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_addrinfo.c.o
[ 33%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_data_into_fd.c.o
[ 33%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_disk_entry_from_file.c.o
[ 33%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_disk_posix.c.o
[ 33%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_ctype.c.o
[ 33%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_des.c.o
[ 33%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_disk_set_standard_lookup.c.o
[ 34%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_endian.c.o
[ 34%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_extract.c.o
[ 34%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_extract2.c.o
[ 34%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_fnmatch.c.o
[ 34%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_open_fd.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_open_file.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_open_filename.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_open_memory.c.o
[ 35%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_get_line.c.o
[ 35%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_gethostname.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_set_format.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_set_options.c.o
[ 35%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_gssapi.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_all.c.o
[ 35%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_memrchr.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_bzip2.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_compress.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_gzip.c.o
[ 35%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_multibyte.c.o
[ 35%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_ntlm_core.c.o
[ 35%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_grzip.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_lrzip.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_lz4.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_lzop.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_none.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_program.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_rpm.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_uu.c.o
[ 36%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_ntlm_wb.c.o
[ 36%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_path.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_xz.c.o
[ 36%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_filter_zstd.c.o
[ 37%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_range.c.o
[ 37%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_7zip.c.o
[ 37%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_rtmp.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_sasl.c.o
[ 38%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_all.c.o
[ 38%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_ar.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_sspi.c.o
[ 38%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_by_code.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/curl_threads.c.o
[ 38%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_cab.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/dict.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/dotdot.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/easy.c.o
[ 38%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_cpio.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/escape.c.o
[ 38%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/file.c.o
[ 39%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/fileinfo.c.o
[ 39%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/formdata.c.o
[ 39%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_empty.c.o
[ 39%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/ftp.c.o
[ 39%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_iso9660.c.o
[ 39%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_lha.c.o
[ 39%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_mtree.c.o
[ 39%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_rar.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_rar5.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_raw.c.o
[ 40%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/url.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_tar.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_warc.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_xar.c.o
[ 40%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/ftplistparser.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_read_support_format_zip.c.o
[ 40%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/getenv.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_string.c.o
[ 40%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/getinfo.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_string_sprintf.c.o
[ 40%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/gopher.c.o
[ 40%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hash.c.o
[ 40%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_util.c.o
[ 41%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hmac.c.o
[ 41%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_version_details.c.o
[ 41%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hostasyn.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_virtual.c.o
[ 42%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hostcheck.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write.c.o
[ 42%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hostip.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_disk_posix.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_disk_set_standard_lookup.c.o
[ 42%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hostip4.c.o
[ 42%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hostip6.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_open_fd.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_open_file.c.o
[ 42%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/hostsyn.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_open_filename.c.o
[ 42%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/http.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_open_memory.c.o
[ 42%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_b64encode.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_by_name.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_bzip2.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_compress.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_grzip.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_gzip.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_lrzip.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_lz4.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_lzop.c.o
[ 43%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_none.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_program.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_uuencode.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_xz.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_add_filter_zstd.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_7zip.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_ar.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_by_name.c.o
[ 44%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/http2.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_cpio.c.o
[ 44%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_cpio_newc.c.o
[ 45%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_filter_by_ext.c.o
[ 45%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_gnutar.c.o
[ 45%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_iso9660.c.o
[ 45%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_mtree.c.o
[ 45%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_pax.c.o
[ 45%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/http_chunks.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/http_digest.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/http_negotiate.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/http_ntlm.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/http_proxy.c.o
[ 46%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_raw.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/idn_win32.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/if2ip.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/imap.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/inet_ntop.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/inet_pton.c.o
[ 46%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_shar.c.o
[ 46%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/krb5.c.o
[ 47%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/ldap.c.o
[ 47%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/llist.c.o
[ 47%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/md4.c.o
[ 47%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/md5.c.o
[ 47%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/memdebug.c.o
[ 47%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/mime.c.o
[ 47%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/mprintf.c.o
[ 47%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_ustar.c.o
[ 47%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_v7tar.c.o
[ 47%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_warc.c.o
[ 48%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_xar.c.o
[ 48%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_format_zip.c.o
[ 48%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/mqtt.c.o
[ 48%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/multi.c.o
[ 48%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/netrc.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/non-ascii.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/nonblock.c.o
[ 49%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_options.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/openldap.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/parsedate.c.o
[ 49%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_write_set_passphrase.c.o
[ 49%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/filter_fork_posix.c.o
[ 49%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/xxhash.c.o
[ 49%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_blake2sp_ref.c.o
[ 49%] Building C object Utilities/cmlibarchive/libarchive/CMakeFiles/cmlibarchive.dir/archive_blake2s_ref.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/pingpong.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/pop3.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/progress.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/psl.c.o
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/doh.c.o
[ 49%] Linking C static library libcmlibarchive.a
[ 49%] Built target cmlibarchive
[ 49%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/rand.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/rename.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/rtsp.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/security.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/select.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/sendf.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/setopt.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/sha256.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/share.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/slist.c.o
[ 50%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/smb.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/smtp.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/socketpair.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/socks.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/socks_gssapi.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/socks_sspi.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/speedcheck.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/splay.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/strcase.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/strdup.c.o
[ 51%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/strerror.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/strtok.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/strtoofft.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/system_win32.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/telnet.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/tftp.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/timeval.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/transfer.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/urlapi.c.o
[ 52%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/version.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/warnless.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/wildcard.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/x509asn1.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/dynbuf.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/cleartext.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/cram.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/digest.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/digest_sspi.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/krb5_gssapi.c.o
[ 53%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/krb5_sspi.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/ntlm.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/ntlm_sspi.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/oauth2.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/spnego_gssapi.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/spnego_sspi.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vauth/vauth.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/bearssl.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/gskit.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/gtls.c.o
[ 54%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/keylog.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/mbedtls.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/mbedtls_threadlock.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/mesalink.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/nss.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/schannel.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/openssl.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/schannel_verify.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/sectransp.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/vtls.c.o
[ 55%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vtls/wolfssl.c.o
[ 56%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vquic/ngtcp2.c.o
[ 56%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vquic/quiche.c.o
[ 56%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vquic/vquic.c.o
[ 56%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vssh/libssh.c.o
[ 56%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vssh/libssh2.c.o
[ 56%] Building C object Utilities/cmcurl/lib/CMakeFiles/cmcurl.dir/vssh/wolfssh.c.o
[ 56%] Linking C static library libcmcurl.a
[ 56%] Built target cmcurl
Scanning dependencies of target curltest
[ 56%] Building C object Utilities/cmcurl/CMakeFiles/curltest.dir/curltest.c.o
Scanning dependencies of target CMakeLib
[ 56%] Linking C executable curltest
[ 56%] Built target curltest
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmCommandArgumentParser.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmCommandArgumentLexer.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmDependsJavaLexer.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmDependsJavaParser.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmExprLexer.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmExprParser.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmFortranLexer.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmFortranParser.cxx.o
[ 56%] Building CXX object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmGccDepfileLexer.cxx.o
[ 57%] Building C object Source/CMakeFiles/CMakeLib.dir/LexerParser/cmListFileLexer.c.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAffinity.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmArchiveWrite.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmArgumentParser.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBase32.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsLinker.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsLinuxELFGetRuntimeDependenciesTool.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsLinuxELFLinker.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsLinuxELFObjdumpGetRuntimeDependenciesTool.cxx.o
[ 57%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsMacOSMachOGetRuntimeDependenciesTool.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsMacOSMachOLinker.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsMacOSMachOOToolGetRuntimeDependenciesTool.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsWindowsPEDumpbinGetRuntimeDependenciesTool.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsWindowsPEGetRuntimeDependenciesTool.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsWindowsPELinker.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBinUtilsWindowsPEObjdumpGetRuntimeDependenciesTool.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCacheManager.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCheckCustomOutputs.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCLocaleEnvironmentScope.cxx.o
[ 58%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCommandArgumentParserHelper.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCommonTargetGenerator.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmComputeComponentGraph.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmComputeLinkDepends.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmComputeLinkInformation.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmComputeTargetDepends.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCPackPropertiesGenerator.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCryptoHash.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCurl.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCustomCommand.cxx.o
[ 59%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCustomCommandGenerator.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCustomCommandLines.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDefinitions.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDepends.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDependsC.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDependsFortran.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDependsJava.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDependsJavaParserHelper.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDocumentation.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDocumentationFormatter.cxx.o
[ 60%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDocumentationSection.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDynamicLoader.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmELF.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExprParserHelper.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportBuildAndroidMKGenerator.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportBuildFileGenerator.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportFileGenerator.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportInstallAndroidMKGenerator.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportInstallFileGenerator.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportTryCompileFileGenerator.cxx.o
[ 61%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportSet.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExternalMakefileProjectGenerator.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExtraCodeBlocksGenerator.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExtraCodeLiteGenerator.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExtraEclipseCDT4Generator.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExtraKateGenerator.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExtraSublimeTextGenerator.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileAPI.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileAPICache.cxx.o
[ 62%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileAPICodemodel.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileAPICMakeFiles.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileCopier.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileInstaller.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileLock.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileLockPool.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileLockResult.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFilePathChecksum.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileTime.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileTimeCache.cxx.o
[ 63%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileTimes.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFortranParserImpl.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFSPermissions.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGccDepfileLexerHelper.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGccDepfileReader.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratedFileStream.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpressionContext.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpressionDAGChecker.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpressionEvaluationFile.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpressionEvaluator.cxx.o
[ 64%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpressionLexer.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpressionNode.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpressionParser.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorExpression.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGeneratorTarget.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLinkItemGraphVisitor.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetPipes.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGlobalCommonGenerator.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGlobalGenerator.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGlobalUnixMakefileGenerator3.cxx.o
[ 65%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGlobVerificationManager.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGraphVizWriter.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallGenerator.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallExportGenerator.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstalledFile.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallFilesGenerator.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallScriptGenerator.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallSubdirectoryGenerator.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallTargetGenerator.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallDirectoryGenerator.cxx.o
[ 66%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLDConfigLDConfigTool.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLDConfigTool.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLinkItem.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLinkLineComputer.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLinkLineDeviceComputer.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmListFileCache.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLocalCommonGenerator.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLocalGenerator.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmRulePlaceholderExpander.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLocalUnixMakefileGenerator3.cxx.o
[ 67%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMakefile.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMakefileTargetGenerator.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMakefileExecutableTargetGenerator.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMakefileLibraryTargetGenerator.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMakefileProfilingData.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMakefileUtilityTargetGenerator.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMessenger.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMSVC60LinkLineComputer.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmOSXBundleGenerator.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmOutputConverter.cxx.o
[ 68%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmNewLineStyle.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmOrderDirectories.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmPolicies.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmProcessOutput.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmProcessTools.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmPropertyDefinition.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmPropertyMap.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQtAutoGen.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQtAutoGenerator.cxx.o
[ 69%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQtAutoGenGlobalInitializer.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQtAutoGenInitializer.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQtAutoMocUic.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQtAutoRcc.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmRST.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmRuntimeDependencyArchive.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmScriptGenerator.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSourceFile.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSourceFileLocation.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSourceGroup.cxx.o
[ 70%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmState.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmStateDirectory.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmStateSnapshot.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmStringAlgorithms.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSystemTools.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTarget.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetPropertyComputer.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTest.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTestGenerator.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmUuid.cxx.o
[ 71%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmUVHandlePtr.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmUVProcessChain.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmVariableWatch.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmVersion.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmWorkerPool.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmWorkingDirectory.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmXMLParser.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmXMLSafe.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmXMLWriter.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmake.cxx.o
[ 72%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCommands.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddCompileDefinitionsCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddCompileOptionsCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddLinkOptionsCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddCustomCommandCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddCustomTargetCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddDefinitionsCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddDependenciesCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddExecutableCommand.cxx.o
[ 73%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddLibraryCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddSubDirectoryCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAddTestCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmAuxSourceDirectoryCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBreakCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBuildCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmBuildNameCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCMakeHostSystemInformationCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCMakeLanguageCommand.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCMakeMinimumRequired.cxx.o
[ 74%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCMakePolicyCommand.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmConditionEvaluator.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmConfigureFileCommand.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmContinueCommand.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCoreTryCompile.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmCreateTestSourceList.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDefinePropertyCommand.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmEnableLanguageCommand.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmEnableTestingCommand.cxx.o
[ 75%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExecProgramCommand.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExecuteProcessCommand.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExpandedCommandArgument.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportCommand.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmExportLibraryDependenciesCommand.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFLTKWrapUICommand.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFileCommand.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFindBase.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFindCommon.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFindFileCommand.cxx.o
[ 76%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFindLibraryCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFindPackageCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFindPathCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFindProgramCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmForEachCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFunctionBlocker.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmFunctionCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetCMakePropertyCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetDirectoryPropertyCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetFilenameComponentCommand.cxx.o
[ 77%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetPropertyCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetSourceFilePropertyCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetTargetPropertyCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGetTestPropertyCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmHexFileConverter.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmIfCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmIncludeCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmIncludeDirectoryCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmIncludeExternalMSProjectCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmIncludeGuardCommand.cxx.o
[ 78%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmIncludeRegularExpressionCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallCommandArguments.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallFilesCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallProgramsCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmInstallTargetsCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLinkDirectoriesCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLinkLibrariesCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmListCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLoadCacheCommand.cxx.o
[ 79%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLoadCommandCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMacroCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMakeDirectoryCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMarkAsAdvancedCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMathCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmMessageCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmOptionCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmOutputRequiredFilesCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmParseArgumentsCommand.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmPathLabel.cxx.o
[ 80%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmProjectCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQTWrapCPPCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmQTWrapUICommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmRemoveCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmRemoveDefinitionsCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmReturnCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSearchPath.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSeparateArgumentsCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSetCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSetDirectoryPropertiesCommand.cxx.o
[ 81%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSetPropertyCommand.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSetSourceFilesPropertiesCommand.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSetTargetPropertiesCommand.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSetTestsPropertiesCommand.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSiteNameCommand.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSourceGroupCommand.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmString.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmStringReplaceHelper.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmStringCommand.cxx.o
[ 82%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSubcommandTable.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSubdirCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmSubdirDependsCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetCompileDefinitionsCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetCompileFeaturesCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetCompileOptionsCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetIncludeDirectoriesCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetLinkOptionsCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetLinkDirectoriesCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetLinkLibrariesCommand.cxx.o
[ 83%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetPrecompileHeadersCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetPropCommandBase.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTargetSourcesCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTimestamp.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTryCompileCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmTryRunCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmUnsetCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmUseMangledMesaCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmUtilitySourceCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmVariableRequiresCommand.cxx.o
[ 84%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmVariableWatchCommand.cxx.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmWhileCommand.cxx.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmWriteFileCommand.cxx.o
[ 85%] Building C object Source/CMakeFiles/CMakeLib.dir/cm_get_date.c.o
[ 85%] Building C object Source/CMakeFiles/CMakeLib.dir/cm_utf8.c.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cm_codecvt.cxx.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmDuration.cxx.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/bindexplib.cxx.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGlobalWatcomWMakeGenerator.cxx.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGlobalGhsMultiGenerator.cxx.o
[ 85%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLocalGhsMultiGenerator.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGhsMultiTargetGenerator.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGhsMultiGpj.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmGlobalNinjaGenerator.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmLocalNinjaGenerator.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmNinjaTargetGenerator.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmNinjaNormalTargetGenerator.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmNinjaUtilityTargetGenerator.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmNinjaLinkLineComputer.cxx.o
[ 86%] Building CXX object Source/CMakeFiles/CMakeLib.dir/cmNinjaLinkLineDeviceComputer.cxx.o
[ 86%] Linking CXX static library libCMakeLib.a
[ 86%] Built target CMakeLib
Scanning dependencies of target CMakeServerLib
Scanning dependencies of target CPackLib
Scanning dependencies of target runcompilecommands
Scanning dependencies of target CTestLib
[ 87%] Building CXX object Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CMakeServerLib.dir/cmConnection.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackArchiveGenerator.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CTestLib.dir/cmCTest.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CMakeServerLib.dir/cmFileMonitor.cxx.o
[ 87%] Linking CXX executable runcompilecommands
[ 87%] Built target runcompilecommands
[ 87%] Building CXX object Source/CMakeFiles/CMakeServerLib.dir/cmJsonObjects.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CMakeServerLib.dir/cmPipeConnection.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CMakeServerLib.dir/cmServer.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackComponentGroup.cxx.o
[ 87%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackDebGenerator.cxx.o
[ 88%] Building CXX object Source/CMakeFiles/CMakeServerLib.dir/cmServerConnection.cxx.o
[ 88%] Building CXX object Source/CMakeFiles/CMakeServerLib.dir/cmServerProtocol.cxx.o
[ 88%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackExternalGenerator.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackGeneratorFactory.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmProcess.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackGenerator.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackLog.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackNSISGenerator.cxx.o
[ 89%] Linking CXX static library libCMakeServerLib.a
[ 89%] Built target CMakeServerLib
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackNuGetGenerator.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestBinPacker.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackSTGZGenerator.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/IFW/cmCPackIFWCommon.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/IFW/cmCPackIFWGenerator.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestBuildAndTestHandler.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/IFW/cmCPackIFWInstaller.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/IFW/cmCPackIFWPackage.cxx.o
[ 89%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestBuildCommand.cxx.o
[ 90%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/IFW/cmCPackIFWRepository.cxx.o
[ 90%] Building CXX object Source/CMakeFiles/CPackLib.dir/CPack/cmCPackRPMGenerator.cxx.o
[ 90%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestBuildHandler.cxx.o
[ 90%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestConfigureCommand.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestConfigureHandler.cxx.o
[ 91%] Linking CXX static library libCPackLib.a
[ 91%] Built target CPackLib
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestCoverageCommand.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestCoverageHandler.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestCurl.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParseMumpsCoverage.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParseCacheCoverage.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParseGTMCoverage.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParseJacocoCoverage.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParseBlanketJSCoverage.cxx.o
[ 91%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParsePHPCoverage.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParseCoberturaCoverage.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmParseDelphiCoverage.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestEmptyBinaryDirectoryCommand.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestGenericHandler.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestHandlerCommand.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestResourceAllocator.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestResourceSpec.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestLaunch.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestMemCheckCommand.cxx.o
[ 92%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestMemCheckHandler.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestMultiProcessHandler.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestReadCustomFilesCommand.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestResourceGroupsLexerHelper.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestRunScriptCommand.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestRunTest.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestScriptHandler.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestSleepCommand.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestStartCommand.cxx.o
[ 93%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestSubmitCommand.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestSubmitHandler.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestTestCommand.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestTestHandler.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestUpdateCommand.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestUpdateHandler.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestUploadCommand.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestUploadHandler.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestVC.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestGlobalVC.cxx.o
[ 94%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestCVS.cxx.o
[ 95%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestSVN.cxx.o
[ 95%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestBZR.cxx.o
[ 95%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestGIT.cxx.o
[ 95%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestHG.cxx.o
[ 95%] Building CXX object Source/CMakeFiles/CTestLib.dir/CTest/cmCTestP4.cxx.o
[ 95%] Building CXX object Source/CMakeFiles/CTestLib.dir/LexerParser/cmCTestResourceGroupsLexer.cxx.o
Scanning dependencies of target testAffinity
[ 95%] Building CXX object Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.o
Scanning dependencies of target pseudo_valgrind
[ 95%] Building CXX object Tests/CMakeLib/PseudoMemcheck/CMakeFiles/pseudo_valgrind.dir/ret0.cxx.o
[ 95%] Linking CXX executable testAffinity
[ 95%] Built target testAffinity
Scanning dependencies of target pseudo_BC
[ 95%] Building CXX object Tests/CMakeLib/PseudoMemcheck/CMakeFiles/pseudo_BC.dir/ret0.cxx.o
[ 95%] Linking CXX executable valgrind
Scanning dependencies of target memcheck_fail
[ 96%] Building CXX object Tests/CMakeLib/PseudoMemcheck/CMakeFiles/memcheck_fail.dir/ret1.cxx.o
[ 96%] Linking CXX static library libCTestLib.a
[ 96%] Built target pseudo_valgrind
Scanning dependencies of target pseudo_purify
[ 96%] Building CXX object Tests/CMakeLib/PseudoMemcheck/CMakeFiles/pseudo_purify.dir/ret0.cxx.o
[ 96%] Built target CTestLib
Scanning dependencies of target CMakeServerLibTests
[ 96%] Building CXX object Tests/CMakeServerLib/CMakeFiles/CMakeServerLibTests.dir/CMakeServerLibTests.cxx.o
[ 96%] Building CXX object Tests/CMakeServerLib/CMakeFiles/CMakeServerLibTests.dir/testServerBuffering.cpp.o
[ 96%] Linking CXX executable BC
[ 96%] Built target pseudo_BC
Scanning dependencies of target ctresalloc
[ 96%] Building CXX object Tests/RunCMake/CMakeFiles/ctresalloc.dir/CTestResourceAllocation/ctresalloc.cxx.o
[ 96%] Linking CXX executable memcheck_fail
[ 96%] Linking CXX executable purify
[ 96%] Built target memcheck_fail
Scanning dependencies of target cpack
[ 97%] Building CXX object Source/CMakeFiles/cpack.dir/CPack/cpack.cxx.o
[ 97%] Built target pseudo_purify
Scanning dependencies of target cmake
[ 97%] Building CXX object Source/CMakeFiles/cmake.dir/cmakemain.cxx.o
[ 97%] Linking CXX executable CMakeServerLibTests
[ 97%] Built target CMakeServerLibTests
[ 97%] Building CXX object Source/CMakeFiles/cmake.dir/cmcmd.cxx.o
[ 97%] Linking CXX executable ../../bin/ctresalloc
[ 97%] Built target ctresalloc
Scanning dependencies of target ctest
[ 97%] Building CXX object Source/CMakeFiles/ctest.dir/ctest.cxx.o
[ 97%] Linking CXX executable ../bin/cpack
Scanning dependencies of target CMakeLibTests
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/CMakeLibTests.cxx.o
[ 98%] Built target cpack
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testArgumentParser.cxx.o
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testCTestBinPacker.cxx.o
[ 98%] Linking CXX executable ../bin/ctest
[ 98%] Built target ctest
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testCTestResourceAllocator.cxx.o
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testCTestResourceSpec.cxx.o
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testCTestResourceGroups.cxx.o
[ 98%] Linking CXX executable ../bin/cmake
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testGccDepfileReader.cxx.o
[ 98%] Built target cmake
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testGeneratedFileStream.cxx.o
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testRST.cxx.o
[ 98%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testRange.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testOptional.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testString.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testStringAlgorithms.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testSystemTools.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testUTF8.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testXMLParser.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testXMLSafe.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testFindPackageCommand.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testUVProcessChain.cxx.o
[ 99%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testUVRAII.cxx.o
[100%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testUVStreambuf.cxx.o
[100%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testCMExtMemory.cxx.o
[100%] Building CXX object Tests/CMakeLib/CMakeFiles/CMakeLibTests.dir/testCMExtAlgorithm.cxx.o
[100%] Linking CXX executable CMakeLibTests
[100%] Built target CMakeLibTests
```
```bash
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CPack/CPack.OSXX11.Info.plist.in
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CPack/CPackWIX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CPack/WIX.template.in
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CPack/NSIS.InstallOptions.ini.in
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CPack/CPack.VolumeIcon.icns.in
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CPack/CPackZIP.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CPack/CPack.OSXX11.main.scpt.in
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/CMakeCheckCompilerFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Internal/FeatureTesting.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindIcotool.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckOBJCXXCompilerFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGLEW.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeJavaCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindX11.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPythonInterp.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeParseImplicitIncludeInfo.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckFortranFunctionExists.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestOBJCCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPatch.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCXXInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineOBJCCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindEclipseCDT4.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI/libver_mpi.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI/mpiver.f90.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI/fortranparam_mpi.f90.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI/libver_mpi.f90.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI/test_mpi.f90.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI/test_mpi.c
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckLinkerFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindRuby.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSDL_net.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeSwiftInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeASMInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/BasicConfigVersion-SameMinorVersion.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindTclStub.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeRCInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestCCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/SystemInformation.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindBoost.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeExportBuildSettings.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/CMakeLists-CXX.txt.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/foo.cpp
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/CMakeLists-C.txt.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/main.f
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/foo.f
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/main.c
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/CMakeLists-Fortran.txt.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/foo.c
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported/main.cpp
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCSharpCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/BundleUtilities.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindThreads.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakePrintHelpers.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckPrototypeDefinition.c.in
-- Installing: /usr/local/share/cmake-3.18/Modules/Squish4RunTestCase.sh
-- Installing: /usr/local/share/cmake-3.18/Modules/FindDevIL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCXXCompilerId.mm.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMotif.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeRCCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgFX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCURL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeASM_NASMInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindFLTK2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindDCMTK.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindASPELL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGLU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIncludeFileCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckCSourceRuns.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindFrameworks.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineOBJCXXCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeAddFortranSubdirectory
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeAddFortranSubdirectory/config_mingw.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeAddFortranSubdirectory/build_mingw.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCSharpCompilerId.cs.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindFreetype.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckFunctionExists.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindJNI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestFortranCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CTestCoverageCollectGCOV.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeParseArguments.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindPackageMode.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLua.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/ExternalData_config.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCheckCompilerFlagCommonPatterns.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/GoogleTestAddTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindEnvModules.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindHg.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckVariableExists.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPerlLibs.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/kde3init_dummy.cpp.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindCodeBlocks.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/MacOSXFrameworkInfo.plist.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeSwiftCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindEXPAT.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/ITKCompatibility.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestBigEndian.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckPrototypeDefinition.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIPOSupported.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindWMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCygwin.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/IntelVSImplicitPath
-- Installing: /usr/local/share/cmake-3.18/Modules/IntelVSImplicitPath/hello.f
-- Installing: /usr/local/share/cmake-3.18/Modules/IntelVSImplicitPath/CMakeLists.txt
-- Installing: /usr/local/share/cmake-3.18/Modules/IntelVSImplicitPath/detect.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/SelectLibraryConfigurations.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGLUT.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/InstallRequiredSystemLibraries.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeVerifyManifest.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FeatureSummary.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForSSTREAM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckFunctionExists.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FindProducer.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UseJava.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGnuTLS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindODBC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindSublimeText2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindDoxygen.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCUDACompilerId.cu.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeExtraGeneratorDetermineCompilerMacrosAndIncludeDirs.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindFLTK.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCUDACompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/SquishTestScript.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIncludeFiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/MatlabTestsRedirect.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLATEX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/exportheader.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/ecos_clean.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForANSIStreamHeaders.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLTTngUST.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPike.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckOBJCXXSourceCompiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckCSourceCompiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckOBJCXXSourceRuns.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestASMCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgParticle.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgAnimation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeMSYSFindMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineJavaCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindWish.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindArmadillo.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindXCTest.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestASM-ATTCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestASM_NASMCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindJPEG.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Use_wxWindows.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgIntrospection.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCXXInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPython.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/GHS_default.gpj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/VS-10.csproj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/VS-7.vcproj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/Xcode-3.pbxproj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/VS-10.vcxproj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/GHS_lib.gpj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/main.swift.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/VS-Intel.vfproj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CompilerId/VS-NsightTegra.vcxproj.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeIOSInstallCombined.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BSDOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/QNX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/MP-RAS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-OpenWatcom-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-windres.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Intel-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsCE-MSVC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-NVIDIA-CUDA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-GNU-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-HP-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Generic-ADSP-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-VisualAge-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-dynamic-XL-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Apple-Swift.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/tvOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-base.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-OpenWatcom-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Absoft-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-MSVC-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/ARTOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-NAG-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Intel-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/DragonFly.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-AppleClang-OBJC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Darwin-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PathScale-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XLClang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Intel-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-HP-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SCO_SV.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Clang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-XL-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PathScale.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-AppleClang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-MSVC-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/FreeBSD.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Clang-OBJC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/GHS-MULTI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PGI-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/iOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU-Fortran-ABI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/MirBSD.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/iOS-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-static-XL-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Flang-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Determine-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-OpenWatcom-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-PathScale-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PGI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-Clang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-arm64-v8a-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-common.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-armeabi-v6-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-mips-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/Determine-Compiler-NDK.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-system.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-armeabi-v7a-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-armeabi-v6-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-stlport_static.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-none.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-mips64-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-common-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-gnustl_shared.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-x86_64-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-c++_shared.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-stlport.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-arm64-v8a-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-x86-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/Determine-Compiler-Standalone.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-mips64-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-x86_64-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-gabi++_static.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-armeabi-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-c++_static.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-mips-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-armeabi-v7a-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-gnustl.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-c++.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/Determine-Compiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-gnustl_static.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-stlport_shared.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-gabi++_shared.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/ndk-stl-gabi++.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-common-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-x86-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android/abi-armeabi-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/kFreeBSD.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-dynamic-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Catamount.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Darwin.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Clang-OBJCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-MSVC-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-GNU-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PGI-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Embarcadero-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/DOS-OpenWatcom-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-static-XL-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-dynamic.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-VisualAge-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-VisualAge-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Generic-ADSP-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/iOS-Initialize.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-GNU-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-dynamic-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-NAG-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Determine.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Fuchsia.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/syllable.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/OS2-OpenWatcom-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Borland-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-PGI-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/DOS-OpenWatcom.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-AppleClang-OBJCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-static-XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Embarcadero.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/OS2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-PGI-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-PGI-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-HP-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-PathScale-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-TinyCC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-static-XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XL-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-dynamic-XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-GNU-OBJC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-GNU-OBJCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/OSF1.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Xenix.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-dynamic-XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Intel-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-static-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/OpenBSD.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-NVIDIA-CUDA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-static-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-PathScale.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-G95-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Darwin-Initialize.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/watchOS-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-dynamic-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-VisualAge-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Euros.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Clang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-static-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-GNU-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-como.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsCE.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-PathScale-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-static-XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-OpenWatcom.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-dynamic-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Absoft-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-dynamic-XL-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/OS2-OpenWatcom.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Intel-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Intel.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Common.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-static-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Generic-ADSP-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-dynamic-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/UnixPaths.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-MSVC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Generic-SDCC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-HP.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-static.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Intel-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-PGI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Initialize.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Embarcadero-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Clang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-dynamic-XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-PGI-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/ULTRIX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPaths.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Haiku.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Apple-Swift.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PGI-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/UnixWare.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/eCos.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-OpenWatcom.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Intel.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Generic.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/NetBSD.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/UNIX_SV.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-static-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Intel-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-windres.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-MSVC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Intel-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Intel-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-VisualAge-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Borland-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-dynamic-XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-Clang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/DOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PathScale-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Generic-ADSP-Common.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-SunPro-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Intel.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/GHS-MULTI-Determine.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-PathScale-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Midipix.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/DOS-OpenWatcom-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/RISCos.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-static-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX/ExportImportList
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU-CXX-ABI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/FreeBSD-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsCE-MSVC-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-VisualAge-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-VisualAge-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-dynamic.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/tvOS-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XLClang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/tvOS-Initialize.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/ARTOS-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-OpenWatcom-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-dynamic-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XLClang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-HP-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SunOS-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-AppleClang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU-C-ABI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Determine-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-static.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Tru64.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/watchOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CYGWIN-GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/AIX-XL-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-PGI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-VisualAge-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Watcom-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Android-Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BeOS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/GNUtoMS_lib.bat.in
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Watcom-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/OpenVMS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-PGI-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsStore-MSVC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-df.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/gas.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/SINIX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Apple-GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneP-static-XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux-CCur-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Linux.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/Windows-Intel-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/GNUtoMS_lib.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/watchOS-Initialize.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/CrayLinuxEnvironment.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/WindowsPhone-MSVC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/BlueGeneQ-base.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/OS2-OpenWatcom-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Platform/HP-UX-GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgGA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSubversion.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeGenericSystem.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindBLAS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPackageMessage.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckCXXCompilerFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindTclsh.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindXercesC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UseJava
-- Installing: /usr/local/share/cmake-3.18/Modules/UseJava/ClearClassFiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindQt4.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/GenerateExportHeader.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeJOMFindMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGCCXML.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLua51.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindIce.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindHDF5.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCXXCompilerABI.cpp
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckOBJCSourceCompiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindIntl.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindHTMLHelp.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCompilerABI.h
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeUnixFindMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgProducer.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGTest.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckLibraryExists.lists.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFortranCompilerId.F.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCSharpCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindQt.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FLTKCompatibility.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCVS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIncludeFile.cxx.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgManipulator.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPythonLibs.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestCXXCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckStructHasMember.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForANSIStreamHeaders.cxx
-- Installing: /usr/local/share/cmake-3.18/Modules/FindQt3.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeASMCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckTypeSizeMap.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FetchContent.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgText.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCABLE.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UseQt4.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/symbol.c.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/mysub.f
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Input.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Output.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/my_sub.f
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/my_module_.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/call_sub.f
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Detect.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/main.F
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/MY_MODULE.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/mymodule.f90
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/call_mod.f90
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Macro.h.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/my_module.f90
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/MYMODULE.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/CMakeLists.txt
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Verify
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Verify/VerifyFortran.f
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Verify/main.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Verify/VerifyCXX.cxx
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Verify/VerifyC.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/Verify/CMakeLists.txt
-- Installing: /usr/local/share/cmake-3.18/Modules/FortranCInterface/mymodule_.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgQt.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenAL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/kde3uic.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCUDAInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindJasper.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindKate.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenThreads.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCUDA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgPresentation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeSystem.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeMinGWFindMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestRCCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Squish4RunTestCase.bat
-- Installing: /usr/local/share/cmake-3.18/Modules/FindBZip2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGTK2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCompilerId.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakePackageConfigHelpers.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeInitializeConfigs.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgTerrain.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSDL_image.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestGNU.c
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSquish.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineASM_MASMCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindBacktrace.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/ExternalProject-gitupdate.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineRCCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindRTI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCXXCompilerABI.mm
-- Installing: /usr/local/share/cmake-3.18/Modules/TestCXXAcceptsFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeAddFortranSubdirectory.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGettext.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CSharpUtilities.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCurses.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLibinput.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCXXCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSDL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UseSWIG
-- Installing: /usr/local/share/cmake-3.18/Modules/UseSWIG/ManageSupportFiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/HP-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-CXX-TestableFeatures.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/VisualAge-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/MSVC-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMCC-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/VisualAge-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PathScale-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GHS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Embarcadero-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/OpenWatcom-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XLClang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Cray-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/TinyCC-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/VisualAge-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SCO-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/MSVC-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PathScale.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PGI-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMClang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMClang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Compaq-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/G95-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Cray.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Flang-FindBinUtils.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/HP-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PathScale-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-CUDA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PathScale-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMCC-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Cray-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/OpenWatcom-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Cray-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PGI-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Borland-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/zOS-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/MSVC-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-FindBinUtils.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XLClang-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/HP-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SDCC-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GHS-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IBMCPP-C-DetermineVersionInternal.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/NVIDIA-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/QCC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GHS-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GHS-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-OBJC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/TI-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/CrayPrgEnv-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/MSVC-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMClang-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Comeau-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-FindBinUtils.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/TinyCC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IAR-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMClang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/CrayPrgEnv.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PGI-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IAR-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/HP-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IAR-FindBinUtils.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ADSP-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/MSVC-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMCC-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IAR-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-OBJC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-OBJCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PGI-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/VisualAge-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Bruce-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PGI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SCO-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/NVIDIA-CUDA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/OpenWatcom.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XLClang.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Fujitsu-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-OBJCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/TI-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/QCC-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Flang-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/QCC-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-DetermineCompilerInternal.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMClang-C-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-OBJCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IAR-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IAR.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/QCC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SunPro-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMClang-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/PathScale-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SCO.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Watcom-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Bruce-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/OpenWatcom-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/TI-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/NAG-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/CCur-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/zOS-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/CrayPrgEnv-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/MSVC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMClang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/QCC-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-Fortran
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XL-Fortran/cpp
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/SCO-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/CrayPrgEnv-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/CMakeCommonCompilerMacros.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Clang-OBJC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/GNU-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/AppleClang-CXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMCC-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Compaq-CXX-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XLClang-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/QCC-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/TI-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Cray-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel-CXX-FeatureTests.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/ARMCC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/VisualAge-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Intel-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/Absoft-Fortran.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/XLClang-C.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/HP-ASM.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/HP-C-DetermineCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Compiler/IBMCPP-CXX-DetermineVersionInternal.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UseJavaSymlinks.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenSceneGraph.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckCXXSourceCompiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenCL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/WriteBasicConfigVersionFile.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindIconv.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindwxWidgets.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCommonLanguageInclude.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/javaTargets.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/AndroidTestUtilities.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/DeployQt4.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindXMLRPC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Dart.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CTestUseLaunchers.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPHP4.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCompileFeatures.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeGraphVizOptions.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCompilerABI.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindImageMagick.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCXXCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgSim.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindDependencyMacro.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckTypeSize.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLibLZMA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindICU.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestCompilerCommon.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindALSA.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLAPACK.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UseJavaClassFilelist.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeAddNewLanguage.txt
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineSwiftCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckSizeOf.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCups.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/BasicConfigVersion-AnyNewerVersion.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckLanguage.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGnuplot.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindBullet.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindProtobuf.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckOBJCCompilerFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindJavaCommon.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDependentOption.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CPack.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeConfigurableFile.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakePlatformId.h.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CTestScriptMode.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineSystem.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenMP.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgViewer.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenACC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeBuildSettings.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckVariableExists.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckForPthreads.c
-- Installing: /usr/local/share/cmake-3.18/Modules/VTKCompatibility.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckCXXSymbolExists.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSDL_mixer.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPython
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPython/Support.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindTIFF.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPerl.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CPackIFW.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPython3.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/GetPrerequisites.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPython2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/MacroAddFileDependencies.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckSymbolExists.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakePushCheckState.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CPackIFWConfigureFile.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGTK.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindJava.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSDL_ttf.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakePrintSystemInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeBorlandFindMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindBISON.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForSSTREAM.cxx
-- Installing: /usr/local/share/cmake-3.18/Modules/UsePkgConfig.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindDart.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindFLEX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgDB.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeSystemSpecificInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/BasicConfigVersion-SameMajorVersion.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/UseEcos.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeASM-ATTInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCXXCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/.NoDartCoverage
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGDAL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineASMCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/GoogleTest.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeSystemSpecificInitialize.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/BasicConfigVersion-ExactVersion.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGSL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIncludeFile.c.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFortranInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestEndianess.c.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCoin3D.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Qt4ConfigDependentSettings.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLua50.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckFortranSourceCompiles.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindXalanC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/KDE3Macros.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/ProcessorCount.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPhysFS.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLibXml2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckIncludeFile.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineCCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCUDAToolkit.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindXCode.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForSTDNamespace.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPEG2.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSelfPackers.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindLibXslt.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckTypeSize.c.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckFortranSourceRuns.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCompilerIdDetection.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestASM_MASMCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgShadow.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckLibraryExists.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UsewxWidgets.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FetchContent
-- Installing: /usr/local/share/cmake-3.18/Modules/FetchContent/CMakeLists.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSDL_sound.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Qt4Macros.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindUnixCommands.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckOBJCSourceRuns.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/MacOSXBundleInfo.plist.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeExpandImportedTargets.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineFortranCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPostgreSQL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindZLIB.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeNMakeFindMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/AndroidTestUtilities
-- Installing: /usr/local/share/cmake-3.18/Modules/AndroidTestUtilities/PushToAndroidDevice.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForANSIForScope.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCUDACompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CTest.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/AddFileDependencies.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindQuickTime.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineASM-ATTCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeNinjaFindMake.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCCompilerABI.c
-- Installing: /usr/local/share/cmake-3.18/Modules/DartConfiguration.tcl.in
-- Installing: /usr/local/share/cmake-3.18/Modules/SquishRunTestCase.sh
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckCXXSourceRuns.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeBackwardCompatibilityCXX.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgWidget.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindAVIFile.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineVSServicePack.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeDetermineASM_NASMCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeBackwardCompatibilityC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgVolume.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindHSPELL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeParseImplicitLinkInfo.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCUDACompilerABI.cu
-- Installing: /usr/local/share/cmake-3.18/Modules/FindFontconfig.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CTestTargets.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPkgConfig.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/RepositoryInfo.txt.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeLanguageInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/ExternalProject-verify.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/FindosgUtil.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindCxxTest.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindKDE3.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/ExternalProject.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindTCL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMatlab.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Documentation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindSQLite3.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeJavaInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMPEG.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Findosg.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CPackComponent.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCCompilerABI.m
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckFortranCompilerFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/SquishRunTestCase.bat
-- Installing: /usr/local/share/cmake-3.18/Modules/DummyCXXFile.cxx
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenSSL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindKDE4.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/ExternalData.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestCSharpCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFortranCompiler.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForSTDNamespace.cxx
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeOBJCCompilerId.m.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestCUDACompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindOpenGL.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/readme.txt
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCSharpInformation.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGIF.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindGit.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckPIESupported.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFortranCompilerABI.F
-- Installing: /usr/local/share/cmake-3.18/Modules/FindwxWindows.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/TestForAnsiForScope.cxx
-- Installing: /usr/local/share/cmake-3.18/Modules/FindMFC.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/Findosg_functions.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/UseSWIG.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeTestJavaCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindPNG.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeForceCompiler.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/FindVulkan.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/WriteCompilerDetectionHeader.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CheckCCompilerFlag.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeImportBuildSettings.cmake
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeCCompilerId.c.in
-- Installing: /usr/local/share/cmake-3.18/Modules/CMakeFindBinUtils.cmake
-- Installing: /usr/local/share/cmake-3.18/Templates
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v12_CL.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v141_CSharp.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_LIB.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v141_CL.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v142_Link.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v12_CSharp.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_RC.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v14_LIB.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_CL.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_CSharp.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v12_RC.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v12_LIB.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_NASM.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v140_CL.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_CSharp.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v140_Link.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_RC.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v142_CL.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_Cuda.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v12_Link.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v142_CSharp.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v141_Link.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_MASM.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v140_CSharp.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v14_RC.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_CL.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_LIB.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v12_MASM.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v14_MASM.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_Link.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_MASM.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v11_Link.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/FlagTables/v10_CudaHost.json
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/nasm.props.in
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/nasm.targets
-- Installing: /usr/local/share/cmake-3.18/Templates/MSBuild/nasm.xml
-- Installing: /usr/local/share/cmake-3.18/Templates/CMakeVSMacros2.vsmacros
-- Installing: /usr/local/share/cmake-3.18/Templates/CPackConfig.cmake.in
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows/SmallLogo.png
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows/Windows_TemporaryKey.pfx
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows/SmallLogo44x44.png
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows/Logo.png
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows/StoreLogo.png
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows/ApplicationIcon.png
-- Installing: /usr/local/share/cmake-3.18/Templates/Windows/SplashScreen.png
-- Installing: /usr/local/share/cmake-3.18/Templates/CPack.GenericLicense.txt
-- Installing: /usr/local/share/cmake-3.18/Templates/CPack.GenericDescription.txt
-- Installing: /usr/local/share/cmake-3.18/Templates/AppleInfo.plist
-- Installing: /usr/local/share/cmake-3.18/Templates/CPack.GenericWelcome.txt
-- Installing: /usr/local/share/cmake-3.18/Templates/TestDriver.cxx.in
-- Installing: /usr/local/share/cmake-3.18/Templates/CMakeVSMacros1.vsmacros
-- Installing: /usr/local/share/cmake-3.18/Templates/CTestScript.cmake.in
-- Installing: /usr/local/share/vim/vimfiles/indent
-- Installing: /usr/local/share/vim/vimfiles/indent/cmake.vim
-- Installing: /usr/local/share/vim/vimfiles/syntax
-- Installing: /usr/local/share/vim/vimfiles/syntax/cmake.vim
-- Installing: /usr/local/share/emacs/site-lisp/cmake-mode.el
-- Installing: /usr/local/share/aclocal/cmake.m4
-- Installing: /usr/local/share/bash-completion/completions/cmake
-- Installing: /usr/local/share/bash-completion/completions/cpack
-- Installing: /usr/local/share/bash-completion/completions/ctest
```

## 7. CMake 설치 확인
```bash
cmake --version
```

**출력 결과**
```bash
user@ubuntu:~/temp/cmake-3.18.1$ cmake --version
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
Modules directory not found in
/usr/local/share/cmake-3.10
cmake version 3.10.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

## 8. CMake를 업데이트하였으나 업데이트 버전 정보가 나오지 않음
```bash
which cmake
ls -l /usr/local/bin/cmake
export PATH=/usr/local/bin:$PATH
cmake --version
```

**출력 결과**
```bash
CMake suite maintained and supported by Kitware (kitware.com/cmake).
user@ubuntu:~/temp/cmake-3.18.1$ which cmake
/usr/local/bin/cmake
user@ubuntu:~/temp/cmake-3.18.1$ ls -l /usr/local/bin/cmake
-rwxr-xr-x 1 root root 9819328  9월 30 18:26 /usr/local/bin/cmake
user@ubuntu:~/temp/cmake-3.18.1$ export PATH=/usr/local/bin:$PATH
user@ubuntu:~/temp/cmake-3.18.1$ cmake --version
cmake version 3.18.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).
user@ubuntu:~/temp/cmake-3.18.1$
```