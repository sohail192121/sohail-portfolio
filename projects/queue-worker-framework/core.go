package workers
import("context";"errors";"sync")
type Job struct{ID string;Payload string}
type Failure struct{ID string;Attempts int;Err error}
func Run(ctx context.Context,jobs <-chan Job,concurrency,attempts int,handler func(context.Context,Job)error)([]Failure,error){if concurrency<1||attempts<1{return nil,errors.New("invalid bounds")};var wg sync.WaitGroup;var mu sync.Mutex;dead:=[]Failure{};for i:=0;i<concurrency;i++{wg.Add(1);go func(){defer wg.Done();for{select{case <-ctx.Done():return;case job,ok:=<-jobs:if !ok{return};var err error;used:=0;for used<attempts{if ctx.Err()!=nil{return};used++;err=handler(ctx,job);if err==nil{break}};if err!=nil{mu.Lock();dead=append(dead,Failure{job.ID,used,err});mu.Unlock()}}}}()};wg.Wait();return dead,ctx.Err()}
