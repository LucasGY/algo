/*

*/
#include<math.h>
#include<time.h>
#include<stdio.h>


typedef int WeightType;
int MAXVertexNum = 100;
typedef struct GNode *PtrToGNode;
struct GNode
{
    int Nv; //图的顶点数
    int Ne; //图的边数
    WeightType G[MAXVertexNum][MAXVertexNum]; //边的存储
    

};



