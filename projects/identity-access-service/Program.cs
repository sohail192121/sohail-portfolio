using System.Security.Cryptography;
using System.Text;
var vault=new Sessions();var now=DateTimeOffset.UtcNow;var token=vault.Issue("user",now.AddHours(1));var next=vault.Rotate(token,now);
if(next is null || vault.Rotate(token,now) is not null)throw new Exception("rotation replay");
vault.Revoke(next);if(vault.Rotate(next,now)is not null)throw new Exception("revocation");
var expired=vault.Issue("user",now.AddSeconds(-1));if(vault.Rotate(expired,now)is not null)throw new Exception("expiry");
if(!Sessions.Allowed(new[]{"admin"},"admin")||Sessions.Allowed(new[]{"reader"},"admin"))throw new Exception("RBAC");
Console.WriteLine("PASS: rotation, expiry, revocation and roles");
sealed class Sessions {
 readonly Dictionary<string,(string User,DateTimeOffset Expiry)> tokens=new();readonly object gate=new();
 static string Hash(string value)=>Convert.ToHexString(SHA256.HashData(Encoding.UTF8.GetBytes(value)));
 public string Issue(string user,DateTimeOffset expiry){if(string.IsNullOrWhiteSpace(user))throw new ArgumentException("user");var token=Convert.ToHexString(RandomNumberGenerator.GetBytes(32));lock(gate)tokens.Add(Hash(token),(user,expiry));return token;}
 public string? Rotate(string token,DateTimeOffset now){lock(gate){if(!tokens.Remove(Hash(token),out var data)||data.Expiry<=now)return null;return Issue(data.User,data.Expiry);}}
 public void Revoke(string token){lock(gate)tokens.Remove(Hash(token));}
 public static bool Allowed(IEnumerable<string> roles,string required)=>roles.Contains(required,StringComparer.Ordinal);
}
