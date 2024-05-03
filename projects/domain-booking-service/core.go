package booking
import("sync";"time";"errors")
type Booking struct{Tenant,Resource,ID string;Start,End time.Time}
type Store struct{mu sync.Mutex;items []Booking}
func(s *Store)Reserve(b Booking)error{if b.Tenant==""||b.Resource==""||b.ID==""||!b.End.After(b.Start){return errors.New("invalid booking")};s.mu.Lock();defer s.mu.Unlock();for _,x:=range s.items{if x.Tenant!=b.Tenant{continue};if x.ID==b.ID{return errors.New("duplicate id")};if x.Resource==b.Resource&&b.Start.Before(x.End)&&x.Start.Before(b.End){return errors.New("overlap")}};s.items=append(s.items,b);return nil}
