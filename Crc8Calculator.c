#include<stdio.h>

int Crc_CalculateCRC8Runtime(short Crc_Length, short Crc_Data[])
{
    short Crc_DataAddr = 0;
    short Crc_LoopCounter = 0;
    short XOR_Value = 0xFF;
    short Crc_poly = 0x1D;
    short init_CRC_Value = 0xFF;
    short Crc_Value;

    init_CRC_Value = 0xFF;
    Crc_Value = init_CRC_Value;
    
    for (Crc_DataAddr = 0; Crc_DataAddr < Crc_Length; Crc_DataAddr++)
    {
        Crc_Value ^= Crc_Data[Crc_DataAddr]; 
        
        for (Crc_LoopCounter = 0; Crc_LoopCounter < 8; Crc_LoopCounter++)
        {
            if ((Crc_Value & 0x80u) > 0)
            {
                Crc_Value = ((Crc_Value << 1)) ^ Crc_poly;
            }
            else
            {
                Crc_Value = (Crc_Value << 1);
            }
        }
    }
    Crc_Value ^= XOR_Value;
    return Crc_Value;
}

int main(void)
{
    short crcRaw[] = {0x70, 0x00, 0x0F, 0xA0, 0xFA, 0x0A, 0x0C}; // 0xD8
    short crcValue;
    crcValue = Crc_CalculateCRC8Runtime(sizeof(crcRaw) / sizeof(crcRaw[0]), crcRaw);
    // sizeof(crcRaw)： 数组总长度的总字节数 / sizeof(crcRaw[0])： 数组单个元素的字节长度
    printf("0x%x", crcValue & 0xFF); // 取数值后2位

    return 0;
}
