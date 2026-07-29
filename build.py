import os
import json

def generate_data():
    data = []
    # 루트 폴더에서 채널 폴더들 찾기
    for channel_name in os.listdir('.'):
        if os.path.isdir(channel_name) and channel_name not in ['.git', '.github', '__pycache__']:
            channel_data = {"name": channel_name, "videos": [], "shorts": []}
            
            # 롱폼/숏폼 폴더 경로
            for type_name, key in [('video', 'videos'), ('short', 'shorts')]:
                path = os.path.join(channel_name, type_name)
                if os.path.exists(path):
                    files = [f for f in os.listdir(path) if f.endswith('.mp4')]
                    for f in files:
                        num = int(''.join(filter(str.isdigit, f)) or 0)
                        channel_data[key].append({
                            "title": f,
                            "url": f"{channel_name}/{type_name}/{f}",
                            "num": num
                        })
                    # 숫자 내림차순 정렬
                    channel_data[key].sort(key=lambda x: x['num'], reverse=True)
            
            data.append(channel_data)
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_data()
