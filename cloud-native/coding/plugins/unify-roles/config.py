# coding:utf8

custom_roles = {
    "配置管理员": {
        "持续部署": ["访问持续部署", "持续部署管理", "删除部署记录"],
        "制品库": ["访问制品库"],
        "Wiki": ["访问Wiki", "编辑Wiki", "删除Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "删除文件", "分享文件"],
        "API文档": ["访问API文档"],
        "代码仓库权限": ["访问代码仓库", "仓库写入", "创建仓库", "版本发布管理", "保护分支设置"],
        "制品仓库权限": ["拉取制品", "删除制品", "推送制品"],
    },
    "产品经理": {
        "项目协同": ["访问项目协同", "编辑迭代", "编辑事项", "删除事项"],
        "Wiki": ["访问Wiki", "编辑Wiki", "删除Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
    },
    "技术经理": {
        "项目协同": ["访问项目协同", "编辑迭代", "删除迭代", "编辑事项", "删除事项"],
        "测试": ["访问测试", "编辑测试计划", "编辑用例", "编辑报告", "执行测试", "删除自动化用例"],
        "代码扫描": ["访问代码扫描", "代码扫描设置"],
        "持续集成": ["访问持续集成", "持续集成管理", "手动触发/停止构建", "删除构建计划", "创建构建计划", "修改构建计划"],
        "持续部署": ["访问持续部署", "持续部署管理", "删除部署记录"],
        "制品库": ["访问制品库"],
        "Wiki": ["访问Wiki", "编辑Wiki", "删除Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "删除文件", "分享文件"],
        "API文档": ["访问API文档"],
        "制品仓库权限": ["拉取制品", "删除制品", "推送制品"],
        "代码仓库权限": ["访问代码仓库", "仓库写入", "创建仓库", "版本发布管理", "保护分支设置", "部署公钥"],
    },
    "需求管理人": {
        "项目协同": ["访问项目协同", "编辑事项", "删除事项"],
        "Wiki": ["访问Wiki", "编辑Wiki", "删除Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
    },
    "需求分析人员": {
        "项目协同": ["访问项目协同", "编辑事项"],
        "Wiki": ["访问Wiki", "编辑Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
    },
    "体验设计人员": {
        "项目协同": ["访问项目协同", "编辑事项"],
        "Wiki": ["访问Wiki", "编辑Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
    },
    "开发组长": {
        "项目协同": ["访问项目协同", "编辑迭代", "删除迭代", "编辑事项", "删除事项"],
        "代码扫描": ["访问代码扫描", "代码扫描设置"],
        "持续集成": ["访问持续集成", "持续集成管理", "手动触发/停止构建", "删除构建计划", "创建构建计划", "修改构建计划"],
        "持续部署": ["访问持续部署", "持续部署管理", "删除部署记录"],
        "制品库": ["访问制品库"],
        "Wiki": ["访问Wiki", "编辑Wiki", "删除Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
        "API文档": ["访问API文档"],
        "代码仓库权限": ["访问代码仓库", "仓库写入", "创建仓库", "版本发布管理", "保护分支设置", "部署公钥"],
        "制品仓库权限": ["拉取制品", "删除制品", "推送制品"],
    },
    "设计开发人员": {
        "项目协同": ["访问项目协同", "编辑迭代", "编辑事项"],
        "代码扫描": ["访问代码扫描"],
        "持续集成": ["访问持续集成", "持续集成管理"],
        "持续部署": ["访问持续部署", "持续部署管理", "删除部署记录"],
        "Wiki": ["访问Wiki", "编辑Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
        "API文档": ["访问API文档"],
        "代码仓库权限": ["访问代码仓库", "仓库写入"],
        "制品仓库权限": ["拉取制品", "推送制品"],
    },
    "测试组长": {
        "项目协同": ["访问项目协同", "编辑迭代", "删除迭代", "编辑事项", "删除事项"],
        "测试": ["访问测试", "编辑测试计划", "编辑用例", "编辑报告", "执行测试", "删除自动化用例"],
        "Wiki": ["访问Wiki", "编辑Wiki", "删除Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
        "API文档": ["访问API文档"],
    },
    "测试人员": {
        "项目协同": ["访问项目协同", "编辑事项", "删除事项"],
        "测试": ["访问测试", "编辑测试计划", "编辑用例", "编辑报告", "执行测试"],
        "Wiki": ["访问Wiki", "编辑Wiki", "分享Wiki"],
        "文件": ["访问文件", "编辑文件", "分享文件"],
        "API文档": ["访问API文档"],
    },
}
