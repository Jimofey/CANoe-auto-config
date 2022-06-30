# encoding: utf-8

CrcRaw = [0x70, 0x00, 0x0F, 0xA0, 0xFA, 0x0A, 0x0C] # 0xD8
# CrcRaw = [0x70, 0xA0] # 0x34

def Crc_CalculateCRC8Runtime(Crc_Length, Crc_Data):

    # This value is XORed to the final register value before returned as the official checksum.
    XOR_Value = 0xFF # Not 0x0

    # Defines the generator polynomial which is used for the CRC algorithm.
    Crc_Poly = 0x1D # Autosar profile 1, #define CRC_POLYNOMIAL_8  (0x1Du)  10000 0000

    # Defines the start condition for the CRC algorithm.
    init_CRC_Value = 0xFF # Default value is not 0x0 absolutely. 
    
    # Checksum value for return.
    Crc_Value = init_CRC_Value
    
    # #10 Perform CRC calculation for each int in Crc_Data
    for Crc_DataAddr in range(0, Crc_Length, 1):

        Crc_Value ^= Crc_Data[Crc_DataAddr]

        # #20 XOR next int of Crc_Data with current CRC value. 
        # This is equivalent to calculating CRC value of concatenated ints.
        for Crc_LoopCounter in range(0, 8, 1):
            if ((Crc_Value & int(0x80)) > 0): 
                # #35 If MSB is 1, CRC value is XORed with polynomial
                Crc_Value = ((Crc_Value << 1)) ^ Crc_Poly
            else:
                Crc_Value = (Crc_Value << 1)

    Crc_Value ^= XOR_Value
    return Crc_Value

if __name__ == '__main__':
    CrcReturn = Crc_CalculateCRC8Runtime(len(CrcRaw), CrcRaw)
    # 整型位宽64bit，高位参与了运算，取数值后2位
    print("0x%x"%(CrcReturn & 0xFF))