package limiter
import("sync";"time";"math")
type bucket struct{tokens float64;at time.Time}
type Limiter struct{mu sync.Mutex;capacity,rate float64;buckets map[string]bucket}
func New(capacity,rate float64)*Limiter{if capacity<=0||rate<=0||math.IsNaN(capacity)||math.IsNaN(rate)||math.IsInf(capacity,0)||math.IsInf(rate,0){panic("invalid policy")};return &Limiter{capacity:capacity,rate:rate,buckets:make(map[string]bucket)}}
func(l *Limiter)Allow(tenant string,now time.Time)bool{if tenant==""{return false};l.mu.Lock();defer l.mu.Unlock();b,ok:=l.buckets[tenant];if !ok{b=bucket{l.capacity,now}};if now.After(b.at){b.tokens=math.Min(l.capacity,b.tokens+now.Sub(b.at).Seconds()*l.rate);b.at=now};allowed:=b.tokens>=1;if allowed{b.tokens--};l.buckets[tenant]=b;return allowed}
