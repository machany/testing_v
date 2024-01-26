#include <stdio.h>

//VS-code에서는 한글 변수명 사용이 힘듬
/*
C언어는 특히 읽기 편하게!
*/

int main(void)
{
    //이것이 주석!
    printf("hello world\n");
    printf("한국어 설정.gg\n");
    
    int N; // 초깃값 설정 (변수선언)
    N = 20; // 초기화 (변수변경)

    printf("%d\n", N); // %d 정수형 값출력!
    /* 이와같은것(%d)을 서식 지정자 라한다
    %nf, %nlf 값이 실수 %c 값이 문자 %s 값이 문자열 */

    int N2 = 30; // 초깃값설정과 동시에 초기화
    printf("%d\n", N2); 

    float cN = 4.32; /* 실수 형식은 소수점6째자리 까지 출력*/
    printf("%f\n", cN);

    return 0;
}

