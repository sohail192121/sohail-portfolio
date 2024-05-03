package workers
import("testing";"context";"errors";"sync/atomic")
func TestRetriesAndDeadLetter(t *testing.T){q:=make(chan Job,1);q<-Job{"1","test"};close(q);var calls atomic.Int32;dead,err:=Run(context.Background(),q,2,3,func(context.Context,Job)error{calls.Add(1);return errors.New("fail")});if err!=nil||len(dead)!=1||calls.Load()!=3{t.Fatal(dead,err,calls.Load())}}
func TestCancellation(t *testing.T){ctx,cancel:=context.WithCancel(context.Background());cancel();_,err:=Run(ctx,make(chan Job),2,3,func(context.Context,Job)error{return nil});if !errors.Is(err,context.Canceled){t.Fatal(err)}}
