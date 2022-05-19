    # def solution(progresses, speeds):
    #     answer = []

    #     day = 0    # 작업 일수 
    #     count = 0  # 작업 개수

    #     while progresses :

    #         if progresses[0] + day*speeds[0] >=100:
    #             progresses.pop(0)
    #             speeds.pop(0) 
    #             count+=1
    #             # 100넘으면 pop해버림 

    #         else:
    #             if count > 0:
    #                 answer.append(count)
    #                 count = 0
    #             day+=1
    #     answer.append(count)



    #     return answer

    def solution(progresses, speeds):
        Q=[]
        for p, s in zip(progresses, speeds):
            print(p,s)
            if len(Q)==0 or Q[-1][0]<-((p-100)//s):
                Q.append([-((p-100)//s),1])
            else:
                Q[-1][1]+=1
        return [q[1] for q in Q]