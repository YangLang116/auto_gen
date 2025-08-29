# Clash 配置生成器

这个工具可以自动从网络上爬取可用的VPN节点信息，并生成可用于Clash的配置文件。

## 订阅地址

#### 地址一:
> https://cdn.jsdelivr.net/gh/YangLang116/auto_gen@master/clash/gen_clash_config.yaml

<img src="qr/jsdelivr.png" width="120px" height="120px"/>

#### 地址二(推荐)：

> https://proxy.v2gh.com/https://raw.githubusercontent.com/YangLang116/auto_gen/refs/heads/master/clash/gen_clash_config.yaml

<img src="qr/v2gh.png"  width="120px" height="120px"/>


## 功能特性

- 支持多种VPN协议：SS、SSR、VMess、Trojan
- 自动从多个来源爬取节点信息
- 生成规范的Clash YAML配置文件
- 内置合理的分流规则

## 使用方法

### 安装依赖

```bash
pip install -r requirements.txt
```

### 生成配置文件

```bash
python generator.py
```

这将在当前目录下生成一个`gen_clash_config.yaml`文件，可以直接用于Clash.

## 注意事项

- 节点可用性可能会随时变化，请定期更新
- 建议多测试几个节点以找到最适合您的网络环境的节点
- 如遇到解析错误，可以尝试修改相应协议的正则表达式 
