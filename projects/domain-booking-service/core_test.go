package booking
import("testing";"time";"sync";"sync/atomic")
func TestBoundaries(t *testing.T){var s Store;t0:=time.Now();b:=Booking{"a","room","1",t0,t0.Add(time.Hour)};if s.Reserve(b)!=nil{t.Fatal("first")};b.ID="2";if s.Reserve(b)==nil{t.Fatal("overlap")};b.Tenant="b";if s.Reserve(b)!=nil{t.Fatal("tenant")};b.Tenant="a";b.Start=b.End;b.End=b.End.Add(time.Hour);if s.Reserve(b)!=nil{t.Fatal("half-open adjacency")}}
func TestConcurrent(t *testing.T){var s Store;var wg sync.WaitGroup;var ok atomic.Int32;start:=time.Now();for i:=0;i<20;i++{wg.Add(1);go func(){defer wg.Done();if s.Reserve(Booking{"a","room","same",start,start.Add(time.Hour)})==nil{ok.Add(1)}}()};wg.Wait();if ok.Load()!=1{t.Fatal(ok.Load())}}
