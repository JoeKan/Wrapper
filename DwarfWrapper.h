#ifndef DwarfWrapper_H
#define DwarfWrapper_H

#include <node.h>
#include <node_object_wrap.h>
#include <string>
#include "./include/DwarfReader.h"
#include "./architecture/ArchBuilder.h"
#include "./architecture/NamespaceRule.h"
#include "./architecture/ClassRule.h"
#include <stdlib.h>
#include <cstdlib>
#include <cassert>
#include <sstream>

using pcv::dwarf::DwarfReader;
using pcv::dwarf::ArchBuilder;
using pcv::dwarf::ArchRule;
using pcv::dwarf::NamespaceRule;
using pcv::dwarf::ClassRule;

class DwarfWrapper : public node::ObjectWrap {
    private:
        DwarfReader* reader_;
        ArchBuilder* arch_;
        
        explicit DwarfWrapper(const std::string &fileName);
        ~DwarfWrapper();

        static v8::Persistent<v8::Function> constructor;
        static void New(const v8::FunctionCallbackInfo<v8::Value>& args);
        static void start(const v8::FunctionCallbackInfo<v8::Value>& args);
        //static void GetArch(Local<String> property, const PropertyCallbackInfo<Value>& info);
        //static void SetArch(Local<String> property, Local<Value> value, const PropertyCallbackInfo<Value>& info);

    public:
        static void Init(v8::Local<v8::Object> exports);
};

#endif