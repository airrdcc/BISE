# Ecommerce Visualization Dashboard

## 项目简介
该项目是一个电商可视化大屏，旨在通过与Hive数据库的交互，展示电商数据的可视化效果。使用Flask框架作为后端，ECharts库作为前端数据可视化工具。

## 文件结构
```
ecommerce-visualization
├── src
│   ├── data
│   │   └── hive_query.py       # 与Hive数据库交互的代码
│   ├── server
│   │   └── app.py               # Flask应用程序入口
│   ├── static
│   │   └── js
│   │       └── echarts.min.js   # ECharts库
│   └── templates
│       └── dashboard.html        # 前端模板
├── requirements.txt              # 项目依赖
└── README.md                     # 项目文档
```

## 功能
- 从Hive数据库中提取电商数据
- 使用ECharts进行数据可视化
- 提供一个Web界面展示可视化结果

## 安装步骤
1. 克隆项目到本地：
   ```
   git clone <repository-url>
   cd ecommerce-visualization
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. 启动应用：
   ```
   python src/server/app.py
   ```

4. 在浏览器中访问 `http://127.0.0.1:5000` 查看可视化大屏。

## 使用说明
 **Hive数据库配置**：确保Hive数据库已正确配置并可访问，且`hive_query.py`中的连接参数（如host、port、username、database等）已根据实际情况修改。
- **自定义查询**：如需展示不同的数据，可修改 `src/data/hive_query.py` 中的SQL查询逻辑，返回你需要的字段和数据格式。
- **前端自定义**：可在 `src/templates/dashboard.html` 中自定义ECharts图表的展示样式和数据绑定方式，实现不同的可视化效果。
- **静态资源**：如需使用本地ECharts库，请将 `echarts.min.js` 放在 `src/static/js/` 目录下，并在模板中正确引用。
- **依赖管理**：如需添加新依赖，建议在虚拟环境下安装，并及时更新 `requirements.txt`.

## 贡献
欢迎任何形式的贡献！请提交问题或拉取请求。

## 许可证
本项目采用MIT许可证。