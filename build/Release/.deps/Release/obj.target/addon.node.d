cmd_Release/obj.target/addon.node := g++ -shared -pthread -rdynamic -m64  -Wl,-soname=addon.node -o Release/obj.target/addon.node -Wl,--start-group Release/obj.target/addon/addon.o Release/obj.target/addon/DwarfWrapper.o Release/obj.target/addon/src/DwarfReader.o Release/obj.target/addon/architecture/ArchBuilder.o Release/obj.target/addon/architecture/NamespaceRule.o Release/obj.target/addon/architecture/ClassRule.o Release/obj.target/addon/src/Context.o Release/obj.target/addon/include/DwarfHelper.o Release/obj.target/addon/src/Type.o -Wl,--end-group -ldwarf -lelf /home/josef/dev/HiWi/DwarfLoader/3rdparty/json11/libjson11.a
