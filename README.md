# MusicStorm

## 整体架构

### 

### 审核

目录结构

.
├── back-end                            # 后端代码
│   ├── mvnw                            # maven wrapper
│   ├── mvnw.cmd                        # maven wrapper for windows
│   ├── pom.xml                         # maven project file
│   ├── src                             # source code
│   └── target                          # target folder
├── database                            # 数据库文件
│   ├── MainSchema.mwb                  # 数据库文件
│   ├── schema.jpg                      # 数据库设计图
│   ├── schema.sql                      # 数据库建表语句
│   ├── starship.sql                    # 建表语句
│   └── weapon.sql                      # 建表语句
├── DevelopmentDocument.md              # 开发文档
├── front-end                           # 前端代码
│   ├── index.html                      # 前端入口文件
│   ├── LICENSE.md                      # 许可证
│   ├── node_modules                    # 前端依赖包
│   ├── package.json                    # 前端依赖配置文件
│   ├── package-lock.json               # 前端依赖锁定文件
│   ├── public                          # 静态资源
│   ├── README.md                       # 项目说明
│   ├── src                             # 前端源码
│   ├── vercel.json                     # vercel 部署配置文件
│   └── vite.config.js                  # vite 打包配置文件
├── LICENSE                             # 许可证
├── materials                           # 设计文件
│   ├── FrontEnd.drawio                 # 前端设计文件
│   ├── FrontEndPageLayers.drawio       # 前端页面层级设计文件
│   └── ThreeLayersDesign.drawio        # 三层架构设计文件
├── README.md                           # 项目说明
└── StarshipProber.pptx                 # 项目演示

整个审核过程无人工，均使用 MindSpore 框架构建的模型

- 文字内容审核
- 音频审核
- 图片审核

### 社区前端

功能：
- 分享对音乐的赏析（图/文/音乐）
- 生成音乐
- 上传音乐
- 播放音乐

### 社区后端

既是社区前端的后端，也是审核的后端o

## 文档要求

- 正文格式
    - 宋体
    - 小四
    - 1.5 倍行距
- 双面打印部分
    - 不要求彩色
- 团队成员的评分表
    - 单面打印
    - 一人一张
- 团队沟通纪要
    - 至少四次
    - 包含内容
        - 参与人
        - 讨论内容
        - 结果
