def main():
    # 个人信息配置
    personal_info = {
        "name": "马悦",
        "title": "北京化工大学计算机科学与技术学士学位，德国xu指数应用大学数据科学硕士在读",
        "description": "多个项目经验，曾任计算机视觉领域的专利设计师和ai大模型评测员",
        "skills": ["Python", "Java", "C++"],
        "projects": [
            {"name": "GitHub主页", "url": "https://github.com/nikk909"}
        ],
        "contact": {
            "email": "yinghua253659@163.com",
            "github": "https://github.com/nikk909"
        }
    }
    
    # HTML模板
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{personal_info['name']} - Tech Card</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
                background-color: #f4f4f4;
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
                text-align: center;
                margin-bottom: 10px;
            }}
            .title {{
                text-align: center;
                color: #666;
                font-size: 1.2em;
                margin-bottom: 20px;
            }}
            .skills {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin: 20px 0;
            }}
            .skill {{
                background: #007bff;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
            }}
            .projects, .contact {{
                margin: 20px 0;
            }}
            a {{
                color: #007bff;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{personal_info['name']}</h1>
            <div class="title">{personal_info['title']}</div>
            <p>{personal_info['description']}</p>
            <h2>技能</h2>
            <div class="skills">
    """
    
    # 添加技能标签
    for skill in personal_info['skills']:
        html_content += f'                <span class="skill">{skill}</span>\n'
    
    html_content += """
            </div>
            <h2>项目经历</h2>
            <div class="projects">
                <ul>
    """
    
    # 添加项目链接
    for project in personal_info['projects']:
        html_content += f'                    <li><a href="{project["url"]}" target="_blank">{project["name"]}</a></li>\n'
    
    html_content += f"""
                </ul>
            </div>
            <h2>联系方式</h2>
            <div class="contact">
                <p>
                    <a href="mailto:{personal_info['contact']['email']}">{personal_info['contact']['email']}</a> |
                    <a href="{personal_info['contact']['github']}" target="_blank">GitHub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # 写入文件
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("index.html generated successfully!")


if __name__ == "__main__":
    main()