import os
import subprocess

def print_ascii_art():
    print("""
              █▓██▓██▓           
        ██▓▓▓ ▓▓▓█▓▓▓▓▓          
         ▓▓▓▓██▓▓▓▓▓▓█▓█         
         █▓▓▓▓█▓█▓▓█ ▓▓▓▓        
        ███▓ ▓█▓▓▓ █▓▓ ▓█        
         ▓█ ▓█▓█▓ ▓▓  ▓          
         █  ▓█▓█▓ ▓▓  ▓          
               █▓                
               █▓                
               ▓▓                
               █▓█               
               █▓                
 ░░▓    ░░░░  █▓▓▓█  ░░░░    ▓░░ 
            ░░▓   ▓░░            
              ░▓░▓░              
              ░▓░▓░              
            ░░▒   ▒░░            
           ░░  ▓ ▓  ░░           
         ░░▓         ▓░░         
 _____          __        __   _     
|  ___|         \ \      / /__| |__  
| |_     _____   \ \ /\ / / _ \ '_ \ 
|  _|   |_____|   \ V  V /  __/ |_) |
|_|                \_/\_/ \___|_.__/ 
    - my Snapchat : tm-8""")

def check_wget():
    """تثبيت wget داخل iSH إذا مو موجود عندك قبل"""
    try:
        subprocess.run(["wget", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("مثبته المكتبه عندك من قبل")
    except FileNotFoundError:
        print("📥 تثبيت wget...")
        if os.path.exists("/etc/alpine-release"):  #  iSH
            try:
                subprocess.run(["apk", "add", "wget"], check=True)
                print("✅ تم التثبيت بنجاح")
            except subprocess.CalledProcessError:
                print("تأكد انك مثبت مكتبة الـ wget")
                exit(1)
        else:
            print("❌ لا يمكن تثبيت wget تلقائيًا، تأكد من تثبيته يدويًا.")
            exit(1)

def download_site(url):
    """تنزيل الموقع باستخدام wget"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    cmd = ['wget', '--mirror', '--convert-links', '--adjust-extension', '--page-requisites', '--no-parent', url]
    print(f"🚀 جاري تحميل السكربت: {url}")
    try:
        subprocess.run(cmd, check=True)
        print("أنتهى تحميل السكربت")
    except subprocess.CalledProcessError:
        print("أوكيشن 🧑🏻‍💼")
        exit(1)

def main():
    print_ascii_art()
    site_url = input("🌍 أدخل رابط الموقع الذي تريد سحبه: ").strip()
    
    if not site_url:
        print("⚠️ لا يمكنك ترك الرابط فارغًا!")
        exit(1)
    
    check_wget()
    download_site(site_url)

if __name__ == "__main__":
    main()