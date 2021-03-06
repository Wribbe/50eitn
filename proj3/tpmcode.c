#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<tss/platform.h>
#include<tss/tss_defines.h>
#include<tss/tss_typedef.h>
#include<tss/tss_structs.h>
#include<tss/tspi.h>
#include<trousers/trousers.h>
#include<tss/tss_error.h>

#define DEBUG 1
#define DBG(message, tResult) { if(DEBUG)  printf("(Line%d, %s) \
%s returned 0x%08x. %s.\n",__LINE__ ,__func__ , message, \
tResult,(char *)Trspi_Error_String(tResult));}

int main( int argc, char **argv ){

//    BYTE *rgbPcrValue, *rgbNumPcrs;
//    UINT32 ulPcrValueLength;
//    UINT32 exitCode, subCapSize, numPcrs, subCap, i, j;

    TSS_HCONTEXT hContext=0;
    TSS_HTPM hTPM = 0;
    TSS_RESULT result;
    TSS_HKEY hSRK = 0;
    TSS_HPOLICY hSRKPolicy=0;
    TSS_UUID SRK_UUID = TSS_UUID_SRK;
    //By default SRK is 20bytes 0
    //takeownership -z
    BYTE wks[20];
    memset(wks,0,20);

    //At the beginning
    //Create context and get tpm handle
    result =Tspi_Context_Create(&hContext);
    DBG("Create a context\n", result);
    result=Tspi_Context_Connect(hContext, NULL);
    DBG("Connect to TPM\n", result);
    result=Tspi_Context_GetTpmObject(hContext, &hTPM);
    DBG("Get TPM handle\n", result);
    //Get SRK handle
    //This operation need SRK secret when you takeownership
    //if takeownership -z the SRK is wks by default
    result=Tspi_Context_LoadKeyByUUID(
            hContext,
            TSS_PS_TYPE_SYSTEM,
            SRK_UUID,
            &hSRK
            );
    DBG("Get SRK handle\n", result);
    result=Tspi_GetPolicyObject(hSRK,
            TSS_POLICY_USAGE, &hSRKPolicy);
    DBG("Get SRK Policy\n", result);
    result=Tspi_Policy_SetSecret(hSRKPolicy,
            TSS_SECRET_MODE_SHA1,20, wks);
    DBG("Tspi_Policy_SetSecret\n", result);

    // Set up parameters for random byte generation.
    UINT32 size_random = 32;
    BYTE * random_bytes = NULL;

    // Generate and print the random bytes.
    Tspi_TPM_GetRandom(hTPM, size_random, &random_bytes);
    printf("Generating %zu random bytes.\n", size_random);
    for (UINT32 i=0; i<size_random; i++) {
        printf("  Random byte #%d: %2x\n", i+1, random_bytes[i]);
    }
    printf("Done with byte-generation.\n");

    // Free random data.
    Tspi_Context_FreeMemory(hTPM, random_bytes);
    DBG("Free memory allocated to random bytes.\n", result);

    // Read values from the first 3 PCR registers.
    printf("Printing values of first 3 PCR registers.\n");
    BYTE * pcr_data_pointer = NULL;
    for (UINT32 i=0; i<3; i++) {
        UINT32 size_pcr_data = 0;
        Tspi_TPM_PcrRead(hTPM, i, &size_pcr_data, &pcr_data_pointer);
        printf("Value in PCR-register#%zu: ", i);
        for (UINT32 j=0; j<size_pcr_data; j++) {
            printf("%2x", pcr_data_pointer[j]);
        }
        printf(".\n");
    }
    printf("Done printing PCR registers.\n");

    //At the end of program
    //Cleanup some object
    result = Tspi_Context_FreeMemory(hContext, NULL);
    DBG("Tspi Context Free Memory\n", result);
    result = Tspi_Context_Close(hContext);
    DBG("Tspi Context Close\n", result);
    return 0;
}

