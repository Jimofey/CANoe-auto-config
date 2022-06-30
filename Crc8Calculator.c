#include<stdio.h>

int Crc_CalculateCRC8Runtime(unsigned int Crc_Length, unsigned int Crc_Data[]){
    int Crc_DataAddr = 0;
    int Crc_LoopCounter = 0;
    int XOR_Value = 0xFF;
    int Crc_poly = 0x1D;
    unsigned int init_CRC_Value = 0xFF;
    unsigned int Crc_Value;

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
            }else
            {
                Crc_Value = (Crc_Value << 1);
            }
        }
    }
    Crc_Value ^= XOR_Value;
    return Crc_Value;
}

int main(){
    unsigned int crcRaw[] = {0x70, 0xA0}, crcValue;
    crcValue = Crc_CalculateCRC8Runtime(sizeof(crcRaw), crcRaw);
    printf("0x%x", crcValue); // 0x34

    return 0;
}
