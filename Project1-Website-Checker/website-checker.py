print("🔎 Website URL checker 🔎")
url = input("\n🌐 Enter the website's URL: ")

if url.startswith('https://'):
    print("🔐 It uses https (secure)")
elif url.startswith('http://'):
    print("🔓 It uses http (not secure)")
else:
    print('this might appear not as a website URL.')
