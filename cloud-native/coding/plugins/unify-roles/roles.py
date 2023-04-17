# coding:utf8

request_body_struct = {
    "applyToAllDepots": True,
    "applyToAllArtifacts": True,
    "permissions": [],
    "depotRolePermissions": [],
    "artifactRolePermissions": [],
}

permissions = {
    "basic": [
        {"function": "ProjectNotice", "action": "View"},  # 通知
        {"function": "ProjectMember", "action": "View"},  # 项目成员查看
        {"function": "ProjectUserRole", "action": "View"},  # 项目用户组查看
        {"function": "ProjectBasicSetting", "action": "View"},  # 基本设置
        {"function": "ProjectActivity", "action": "View"},  # 活动日志查看
    ],
    "项目协同/访问项目协同": [
        {"function": "ProjectAgile", "action": "View"},
    ],
    "项目协同/编辑迭代": [
        {"function": "ProjectAgile", "action": "View"},
        {
            "function": "ProjectIteration",
            "action": "Create",
        },
        {
            "function": "ProjectIteration",
            "action": "Update",
        },
    ],
    "项目协同/删除迭代": [
        {"function": "ProjectAgile", "action": "View"},
        {
            "function": "ProjectIteration",
            "action": "Delete",
        },
    ],
    "项目协同/编辑事项": [
        {"function": "ProjectAgile", "action": "View"},
        {
            "function": "ProjectIssue",
            "action": "Create",
        },
        {
            "function": "ProjectIssue",
            "action": "Update",
        },
    ],
    "项目协同/删除事项": [
        {"function": "ProjectAgile", "action": "View"},
        {
            "function": "ProjectIssue",
            "action": "Delete",
        },
    ],
    "测试/访问测试": [
        {"function": "ProjectTest", "action": "View"},
    ],
    "测试/编辑测试计划": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestRun",
            "action": "Create",
        },
        {
            "function": "ProjectTestRun",
            "action": "Update",
        },
    ],
    "测试/归档测试计划": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestRun",
            "action": "Archive",
        },
    ],
    "测试/删除测试计划": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestRun",
            "action": "Delete",
        },
    ],
    "测试/编辑用例": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestCase",
            "action": "Create",
        },
        {
            "function": "ProjectTestCase",
            "action": "Update",
        },
    ],
    "测试/删除用例": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestCase",
            "action": "Delete",
        },
    ],
    "测试/编辑报告": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestReport",
            "action": "Create",
        },
        {
            "function": "ProjectTestReport",
            "action": "Update",
        },
    ],
    "测试/删除报告": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestReport",
            "action": "Delete",
        },
    ],
    "测试/执行测试": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestResult",
            "action": "Create",
        },
    ],
    "测试/编辑自动化用例": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestAutomationCase",
            "action": "Create",
        },
        {
            "function": "ProjectTestAutomationCase",
            "action": "Update",
        },
    ],
    "测试/删除自动化用例": [
        {"function": "ProjectTest", "action": "View"},
        {
            "function": "ProjectTestAutomationCase",
            "action": "Delete",
        },
    ],
    "代码扫描/访问代码扫描": [
        {"function": "ProjectCodeAnalysis", "action": "View"},
    ],
    "代码扫描/代码扫描设置": [
        {"function": "ProjectCodeAnalysis", "action": "Update"},
    ],
    "持续集成/访问持续集成": [
        {"function": "ProjectCI", "action": "View"},
    ],
    "持续集成/持续集成管理": [
        {"function": "ProjectCI", "action": "View"},
        {
            "function": "ProjectCiBuild",
            "action": "Exec",
        },
        {"function": "ProjectCI", "action": "Reset"},
        {"function": "ProjectCI", "action": "Delete"},
        {"function": "ProjectCI", "action": "Update"},
        {"function": "ProjectCI", "action": "Create"},
        {"function": "ProjectCI", "action": "Copy"},
        {"function": "ProjectCI", "action": "Manage"},
        {
            "function": "ProjectCiBuild",
            "action": "Delete",
        },
    ],
    "持续集成/手动触发/停止构建": [
        {"function": "ProjectCI", "action": "View"},
        {
            "function": "ProjectCiBuild",
            "action": "Exec",
        },
    ],
    "持续集成/重置缓存": [
        {"function": "ProjectCI", "action": "View"},
        {"function": "ProjectCI", "action": "Reset"},
    ],
    "持续集成/删除构建计划": [
        {"function": "ProjectCI", "action": "View"},
        {"function": "ProjectCI", "action": "Delete"},
    ],
    "持续集成/修改构建计划": [
        {"function": "ProjectCI", "action": "View"},
        {"function": "ProjectCI", "action": "Update"},
    ],
    "持续集成/创建构建计划": [
        {"function": "ProjectCI", "action": "View"},
        {"function": "ProjectCI", "action": "Create"},
    ],
    "持续集成/管理构建计划": [
        {"function": "ProjectCI", "action": "View"},
        {"function": "ProjectCI", "action": "Manage"},
    ],
    "持续集成/复制构建计划": [
        {"function": "ProjectCI", "action": "View"},
        {"function": "ProjectCI", "action": "Copy"},
    ],
    "持续集成/删除构建记录": [
        {"function": "ProjectCI", "action": "View"},
        {
            "function": "ProjectCiBuild",
            "action": "Delete",
        },
    ],
    "持续部署/访问持续部署": [
        {"function": "ProjectCD", "action": "View"},
    ],
    "持续部署/持续部署管理": [
        {"function": "ProjectCD", "action": "View"},
        {
            "function": "ProjectDeliveryOrder",
            "action": "Create",
        },
    ],
    "持续部署/删除部署记录": [
        {"function": "ProjectCD", "action": "View"},
        {
            "function": "ProjectStaticPages",
            "action": "View",
        },
        {
            "function": "ProjectStaticPages",
            "action": "Delete",
        },
        {
            "function": "ProjectStaticPages",
            "action": "Create",
        },
        {
            "function": "ProjectStaticPages",
            "action": "Update",
        },
    ],
    "制品库/访问制品库": [
        {"function": "ProjectArtifact", "action": "View"},
    ],
    "制品库/制品库设置": [
        {"function": "ProjectArtifact", "action": "View"},
        {
            "function": "ProjectArtifact",
            "action": "Create",
        },
    ],
    "制品库/删除制品仓库": [
        {"function": "ProjectArtifact", "action": "View"},
        {
            "function": "ProjectArtifact",
            "action": "Delete",
        },
    ],
    "Wiki/访问Wiki": [
        {"function": "ProjectWiki", "action": "View"},
    ],
    "Wiki/编辑Wiki": [
        {"function": "ProjectWiki", "action": "View"},
        {"function": "ProjectWiki", "action": "Create"},
        {"function": "ProjectWiki", "action": "Update"},
    ],
    "Wiki/删除Wiki": [
        {"function": "ProjectWiki", "action": "View"},
        {"function": "ProjectWiki", "action": "Delete"},
    ],
    "Wiki/分享Wiki": [
        {"function": "ProjectWiki", "action": "View"},
        {"function": "ProjectWikiShare", "action": "Create"},
        {"function": "ProjectWikiShare", "action": "Delete"},
    ],
    "文件/访问文件": [
        {"function": "ProjectFile", "action": "View"},
    ],
    "文件/编辑文件": [
        {"function": "ProjectFile", "action": "View"},
        {"function": "ProjectFile", "action": "Create"},
        {"function": "ProjectFile", "action": "Update"},
    ],
    "文件/删除文件": [
        {"function": "ProjectFile", "action": "View"},
        {"function": "ProjectFile", "action": "Delete"},
    ],
    "文件/分享文件": [
        {"function": "ProjectFile", "action": "View"},
        {"function": "ProjectFileShare", "action": "Create"},
        {"function": "ProjectFileShare", "action": "Delete"},
    ],
    "API文档/访问API文档": [
        {"function": "ProjectApiDoc", "action": "View"},
    ],
    "访问审计/敏感标记": [
        {"function": "ProjectSensitiveResource", "action": "View"},
        {"function": "ProjectSensitiveResource", "action": "Create"},
        {"function": "ProjectSensitiveResource", "action": "Delete"},
    ],
    "设置/项目公告管理": [
        {"function": "ProjectNotice", "action": "Create"},
        {"function": "ProjectNotice", "action": "Update"},
        {"function": "ProjectNotice", "action": "Delete"},
    ],
    "设置/分类标签管理": [
        {"function": "ProjectLabel", "action": "View"},
        {"function": "ProjectLabel", "action": "Create"},
        {"function": "ProjectLabel", "action": "Update"},
        {"function": "ProjectLabel", "action": "Delete"},
    ],
    "设置/团队筛选器配置": [
        {"function": "ProjectIssueFilter", "action": "Create"},
        {"function": "ProjectIssueFilter", "action": "Update"},
        {"function": "ProjectIssueFilter", "action": "Delete"},
    ],
    "设置/模块管理": [
        {"function": "ProjectModule", "action": "Create"},
        {"function": "ProjectModule", "action": "Update"},
        {"function": "ProjectModule", "action": "Delete"},
    ],
    "设置/协同项目配置": [
        {
            "function": "ProjectIssueCustomFieldAndWorkFlow",
            "action": "Update",
        },
    ],
    "设置/关联仓库管理": [
        {"function": "ExternalDepot", "action": "View"},
        {"function": "ExternalDepot", "action": "Update"},
    ],
    "设置/webhook": [
        {"function": "ProjectWebHook", "action": "View"},
        {"function": "ProjectWebHook", "action": "Create"},
        {"function": "ProjectWebHook", "action": "Update"},
        {"function": "ProjectWebHook", "action": "Delete"},
    ],
    "设置/项目令牌": [
        {"function": "ProjectDeployToken", "action": "View"},
        {"function": "ProjectDeployToken", "action": "Update"},
        {"function": "ProjectDeployToken", "action": "Create"},
        {"function": "ProjectDeployToken", "action": "Delete"},
    ],
    "设置/模板管理": [
        {"function": "ProjectMarkdownTemplate", "action": "View"},
        {"function": "ProjectMarkdownTemplate", "action": "Create"},
        {"function": "ProjectMarkdownTemplate", "action": "Update"},
        {"function": "ProjectMarkdownTemplate", "action": "Delete"},
    ],
    "设置/凭据管理": [
        {"function": "ProjectServiceConn", "action": "Create"},
        {"function": "ProjectServiceConn", "action": "Update"},
        {"function": "ProjectServiceConn", "action": "View"},
        {"function": "ProjectServiceConn", "action": "Delete"},
    ],
    "代码仓库权限/访问代码仓库": [
        {"function": "ProjectDepot", "action": "View"},
    ],
    "代码仓库权限/仓库写入": [
        {"function": "ProjectDepot", "action": "View"},
        {"function": "ProjectDepot", "action": "Update"},
    ],
    "代码仓库权限/创建仓库": [
        {"function": "ProjectDepot", "action": "View"},
        {"function": "ProjectDepot", "action": "Create"},
    ],
    "代码仓库权限/版本发布管理": [
        {"function": "ProjectDepot", "action": "View"},
        {"function": "ProjectRelease", "action": "Create"},
        {"function": "ProjectRelease", "action": "Update"},
        {"function": "ProjectRelease", "action": "Delete"},
    ],
    "代码仓库权限/保护分支设置": [
        {"function": "ProjectDepot", "action": "View"},
        {"function": "ProjectGitProtectedBranch", "action": "Create"},
    ],
    "代码仓库权限/部署公钥": [
        {"function": "ProjectDeployKey", "action": "View"},
        {"function": "ProjectDeployKey", "action": "Update"},
        {"function": "ProjectDeployKey", "action": "Create"},
        {"function": "ProjectDeployKey", "action": "Delete"},
    ],
    "代码仓库权限/解锁锁定文件": [
        {"function": "ProjectDeployKey", "action": "View"},
        {"function": "ProjectGitLFSLock", "action": "Delete"},
    ],
    "制品仓库权限/拉取制品": [
        {"function": "ProjectArtifactAll", "action": "View"},
    ],
    "制品仓库权限/删除制品": [
        {"function": "ProjectArtifactAll", "action": "Delete"},
    ],
    "制品仓库权限/推送制品": [
        {"function": "ProjectArtifactAll", "action": "Create"},
    ],
}
