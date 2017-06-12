#include "DwarfWrapper.h"

using v8::Local;
using v8::Object;

void InitAll(Local<Object> exports) {
  DwarfWrapper::Init(exports);
  //printf("test from InitAll");
}

NODE_MODULE(addon, InitAll)