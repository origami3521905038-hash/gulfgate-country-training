# 阿语听音接入

公网播放页：`https://gulfgate-arabic-audio.awake-cake-3719.chatgpt.site/player.html`

本轮词汇链接格式：`https://gulfgate-arabic-audio.awake-cake-3719.chatgpt.site/player.html?terms=id1,id2,id3`

## 开篇必须给入口

每个新训练会话的首轮回复都要加一小段听音提醒，放在情景式开场之后、六项建档问题之前；不要求用户先打开页面才能继续训练。同一会话只完整提示一次，用户之后要求重发时再给。

可用话术：

> 路上遇到阿拉伯语，可以随时用“阿语随身听”听发音：https://gulfgate-arabic-audio.awake-cake-3719.chatgpt.site/player.html。剧情里出现已收录的词，我会把本轮全部词汇合并到一个点读入口。
>
> 阿语随身听：https://gulfgate-arabic-audio.awake-cake-3719.chatgpt.site/player.html

公网地址不可用或用户明确要求离线使用时，才改用包内播放器，并补一句：“这是本机离线页面，请在保存了技能包的同一台电脑上打开，并保持文件夹完整。”

## 公网地址与离线后备

- 默认使用已部署的公网播放页。包内同时保留 [player.html](../assets/arabic-audio/player.html)、[terms.json](../assets/arabic-audio/terms.json)、379 条词条与 369 段 MP3，作为离线后备；音频相对播放页保存在 `assets/audio/`，不能单独移动 HTML。
- 有 Python 时运行 `python "<实际技能目录>/assets/arabic-audio/scripts/lookup.py" --stats` 确认包可读，再把播放器绝对路径转换为 `file://` 入口网址。也可查询任一确定词，从返回的 `page_url` 移除末尾 `#<id>` 后作为入口。脚本以自身位置解析路径，不依赖当前工作目录，也不写死本机地址。
- 确认入口与音频目录可读后，给出符合宿主格式的文件链接，并额外将返回的完整 `page_url` 放在独立代码块中，方便复制到外部浏览器地址栏；不要只显示链接标题。代码块内的 file URI 是供用户复制的地址，不是可跨设备访问的网址。
- 无 Python 时按实际文件系统位置定位播放页，输出完整文件路径，提示复制到本机浏览器地址栏；不要编造路径。
- 如果技能在远程沙盒运行，远程文件地址不能当成用户本机地址。优先使用上面的 HTTPS 播放页；确实不可访问时，交付完整播放目录供用户下载解压，并提示双击 `player.html`。无法交付文件时如实说明，不输出虚假链接。
- 手机或跨设备使用需要已部署的 HTTPS 页面及同目录音频。没有真实部署结果不得猜测域名，也不因启用训练就自动发布。仅上传知识库文本不会部署 HTML 或 MP3 文件。

## 剧情词本轮合并链接

每次生成剧情、C1/C2/C3、选项、反馈或知识卡后，发送前找出实际出现的阿语原文、拉丁转写和明确作为阿语术语使用的英文词名，逐个运行 `python "<实际技能目录>/assets/arabic-audio/scripts/lookup.py" "<词>"`。

- 只有 `status=ok` 且 `audio_exists=true` 时，才记录返回的词条 `id`。扫描本轮全部阿语词后，按首次出现顺序去重，把所有 ID 用英文逗号连接到 `player.html?terms=` 后，整轮只生成一个“🎧 本轮词汇点读”链接。公网模式使用公网播放页；离线模式对包内 `player.html` 使用相同查询参数。
- 同一词在同一回复中重复时只记录一次；不同已收录词全部进入同一个链接。命中多少个不同词就写入多少个 ID，没有单轮上限；即使两个不同词共用同一段 MP3，也分别保留两个词条 ID。不得为了缩短链接而回避必要术语、删减词义介绍、只挑代表词或让用户自行搜索。
- 只要本轮命中一个或多个音频词条，就在整段回复最下方先给一次本轮词汇入口，例如 `🎧 本轮词汇点读：[打开本轮 3 个词](https://gulfgate-arabic-audio.awake-cake-3719.chatgpt.site/player.html?terms=gahwa,majlis,in-sha-allah)`；再另起一行给一次 `🎧 完整阿语随身听：[打开全部词库](https://gulfgate-arabic-audio.awake-cake-3719.chatgpt.site/player.html)`。
- `status=not_found` 时只保留文字；`status=ambiguous` 时先结合剧情消歧，仍不能唯一确定就不附链接；音频缺失时不提供失效链接。
- 用户询问发音或要求重开入口时，沿用同一查询规则。未命中可说明“这个词暂未收录音频”，继续提供原术语文字，不用近似词的音频替代。

示例正文仍完整介绍每个词；回复底部统一输出：`🎧 本轮词汇点读：[打开本轮 3 个词](https://gulfgate-arabic-audio.awake-cake-3719.chatgpt.site/player.html?terms=gahwa,majlis,in-sha-allah)`。

支持阿语、转写和词表别名。本轮链接使用查询参数，不依赖 `#` 锚点；播放器会只展示链接中有效的词条 ID。无脚本环境可读取词表精确匹配别名并核对音频存在；不把未收录词声称为可播放，不在线合成新发音。

本轮页面只显示“本轮词汇 · N 个”和下方普通词条，不显示额外操作提示句，也不显示完整词库的吸顶筛选区；页面不自动播放，也不提供本轮强制连播，由用户自行选择是否播放以及点击哪个词的发音。完整词库页面顶部的“⌕ 查找与筛选”默认收起，点击后展开，再次点击即可收回。音频来自 macOS Majed 机器合成，按主题组织为商务词表，并配套标准转写、中文音译与业务释义。`Kayf halak / Kayf halik` 与 `Min fadlak / Min fadlik` 的男女词尾版本共用音频。页面不接收或同步笔记、训练答案、档案；打开或播放不计为训练完成或能力证据。
