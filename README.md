# CANoeAutoConfig
Config CANoe via python. Python脚本调用CANoe的COM接口实现CANoe的自动化配置。

1. XCPVariableConfig  
参考脚本注释,读取的变量文件（Excel)应以单列多行形式列举变量，且不带前缀。  
相对应的.[ ]等符号的转换应与XCP窗口传入的表述一致。

2. Crc8Calculator  
CRC8的手动校验，注意初始值的不同，AUTOSAR新规定为0xFF。  

3. DBCSignalSorting  
从DBC文件中提取定义的信号，常用于CAN信号测试，参考Crc8Calculator.can。  
 - ❌CAPL语法不支持变量的定义时赋值：int a = 1;
