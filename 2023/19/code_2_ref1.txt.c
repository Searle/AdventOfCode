#include <stdbool.h>
#include <stdio.h>

bool c_px(int x, int m, int a, int s);
bool c_pv(int x, int m, int a, int s);
bool c_lnx(int x, int m, int a, int s);
bool c_rfg(int x, int m, int a, int s);
bool c_qs(int x, int m, int a, int s);
bool c_qkq(int x, int m, int a, int s);
bool c_crn(int x, int m, int a, int s);
bool c_in(int x, int m, int a, int s);
bool c_qqz(int x, int m, int a, int s);
bool c_gd(int x, int m, int a, int s);
bool c_hdj(int x, int m, int a, int s);

bool c_px(int x, int m, int a, int s) {
    if (a<2006) return c_qkq(x,m,a,s);
    if (m>2090) return true;
    return c_rfg(x,m,a,s);
}
bool c_pv(int x, int m, int a, int s) {
    if (a>1716) return false;
    return true;
}
bool c_lnx(int x, int m, int a, int s) {
    if (m>1548) return true;
    return true;
}
bool c_rfg(int x, int m, int a, int s) {
    if (s<537) return c_gd(x,m,a,s);
    if (x>2440) return false;
    return true;
}
bool c_qs(int x, int m, int a, int s) {
    if (s>3448) return true;
    return c_lnx(x,m,a,s);
}
bool c_qkq(int x, int m, int a, int s) {
    if (x<1416) return true;
    return c_crn(x,m,a,s);
}
bool c_crn(int x, int m, int a, int s) {
    if (x>2662) return true;
    return false;
}
bool c_in(int x, int m, int a, int s) {
    if (s<1351) return c_px(x,m,a,s);
    return c_qqz(x,m,a,s);
}
bool c_qqz(int x, int m, int a, int s) {
    if (s>2770) return c_qs(x,m,a,s);
    if (m<1801) return c_hdj(x,m,a,s);
    return false;
}
bool c_gd(int x, int m, int a, int s) {
    if (a>3333) return false;
    return false;
}
bool c_hdj(int x, int m, int a, int s) {
    if (m>838) return true;
    return c_pv(x,m,a,s);
}

// x_list: 4
int x_list[] = {1,1415,1416,1025,2441,222,2663,1338};
int x_list_size = sizeof(x_list) / sizeof(x_list[0]);
// m_list: 5
int m_list[] = {1,838,839,710,1549,252,1801,290,2091,1910};
int m_list_size = sizeof(m_list) / sizeof(m_list[0]);
// a_list: 4
int a_list[] = {1,1716,1717,289,2006,1328,3334,667};
int a_list_size = sizeof(a_list) / sizeof(a_list[0]);
// s_list: 5
int s_list[] = {1,536,537,814,1351,1420,2771,678,3449,552};
int s_list_size = sizeof(s_list) / sizeof(s_list[0]);

void main() {
    long long result = 0;
    for (int xi= 0; xi < x_list_size; xi += 2) {
        int x= x_list[xi];
        int x2= x_list[xi + 1];
        for (int mi= 0; mi < m_list_size; mi += 2) {
            int m= m_list[mi];
            int m2= m_list[mi + 1];
            for (int ai= 0; ai < a_list_size; ai += 2) {
                int a= a_list[ai];
                int a2= a_list[ai + 1];
                long long xma2= (long long)x2 * (long long)m2 * (long long)a2;
                for (int si= 0; si < s_list_size; si += 2) {
                    int s= s_list[si];
                    int s2= s_list[si + 1];
                    if (c_in(x,m,a,s)) result += xma2 * s2;
                }
            }
        }
    }
    printf("RESULT: %lld\n", result);
}
