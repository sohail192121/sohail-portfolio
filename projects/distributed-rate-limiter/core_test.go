package limiter
import("testing";"time";"sync";"sync/atomic")
func TestRefillAndTenant(t *testing.T){l:=New(1,1);now:=time.Now();if !l.Allow("a",now)||l.Allow("a",now)||!l.Allow("b",now)||!l.Allow("a",now.Add(time.Second)){t.Fatal("bucket invariant")}}
func TestConcurrent(t *testing.T){l:=New(10,1);now:=time.Now();var accepted atomic.Int32;var wg sync.WaitGroup;for i:=0;i<100;i++{wg.Add(1);go func(){defer wg.Done();if l.Allow("a",now){accepted.Add(1)}}()};wg.Wait();if accepted.Load()!=10{t.Fatal(accepted.Load())}}
