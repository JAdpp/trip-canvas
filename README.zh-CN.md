![Sticker Travel Scrapbook banner](assets/brand/banner.jpg)

# 贴纸旅行手帐

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

`sticker-travel-scrapbook` 是一个 Codex Skill，用来创建、规划、修改和交互式编辑东亚贴纸风旅行手帐页面与小漫画旅行日记。

它的重点不是规整的旅行攻略或照片书，而是记忆优先的视觉创作：场景、情绪、同行者、食物、小物件、票据感碎片、照片槽位、贴纸、胶带和小漫画瞬间。

## 示例图集

下面是公开安全的生成示例，不包含私人旅行照片、商业角色、品牌吉祥物、真实票据或私人肖像。

<table>
  <tr>
    <td width="44%" rowspan="2" valign="top">
      <strong>长条页：京都雨天寺社街</strong><br>
      <img src="assets/examples/kyoto-rainy-temple.jpg" alt="京都雨天寺社街手帐示例" width="100%">
    </td>
    <td width="56%" valign="top">
      <strong>单页：首尔韩屋村与夜市</strong><br>
      <img src="assets/examples/seoul-hanok-market.jpg" alt="首尔韩屋村夜市手帐示例" width="100%">
    </td>
  </tr>
  <tr>
    <td width="56%" valign="top">
      <strong>双页：台湾海岸火车与灯笼老街</strong><br>
      <img src="assets/examples/taiwan-coastal-train.jpg" alt="台湾海岸火车手帐示例" width="100%">
    </td>
  </tr>
</table>

## 这个 Skill 能做什么

- 把旅行素材整理成适合手帐创作的记忆场景。
- 规划东亚贴纸风版式、小漫画版式和混合拼贴版式。
- 生成可编辑对象清单，并使用 `P1-IMG1`、`P1-TXT1`、`P1-CHR1`、`P1-STK1`、`P1-PNL1` 等稳定 ID。
- 维持多页之间的角色和视觉风格一致性。
- 生成可复制到图像模型中的新图 prompt 或局部修改 prompt。
- 支持只替换某个照片槽、贴纸、文字卡片或漫画分镜，而不重做整页。
- 提供本地网页 GUI，用于编辑项目、生成 prompt、导入导出 JSON，以及在配置 API key 后直接生图。

## 仓库结构

```text
Sticker-Travel-Scrapbook/
  SKILL.md
  README.md
  README.zh-CN.md
  README.ja.md
  agents/
    openai.yaml
  scripts/
    server.py
  assets/
    brand/
      banner.jpg
    examples/
      kyoto-rainy-temple.jpg
      seoul-hanok-market.jpg
      taiwan-coastal-train.jpg
    gui/
      index.html
      blank-project.json
      demo-project.json
  references/
    authoring-workflow.md
    memory-structure.md
    east-asian-visual-language.md
    comic-panel-patterns.md
    character-consistency.md
    editable-object-manifest.md
    prompt-template.md
    revision-protocol.md
    qa-checklist.md
    gui-workflow.md
    public-asset-policy.md
    default-config.yaml
    character-profile.example.yaml
```

## 安装

把这个仓库文件夹复制到 Codex 的 skills 目录，并把文件夹名保持为 `sticker-travel-scrapbook`。

Windows 用户常见位置：

```powershell
C:\Users\<you>\.codex\skills\sticker-travel-scrapbook
```

如果 Codex 没有立刻识别 Skill，可以重启 Codex 或开启一个新线程。

## 在 Codex 中使用

可以显式调用这个 Skill：

```text
Use $sticker-travel-scrapbook。
我想做一张东亚贴纸风旅行手帐/小漫画页面。

旅行内容：
6 月 19 日，城市乐园夜游，夏日祭。重点记忆包括夜间灯光、小型巡游、过山车、小吃、烟花、在人群中散步返程。整体情绪是兴奋、热闹、有庆祝感。

请输出：
1. 旅行记忆结构表
2. 页面形式与版式建议
3. 可编辑对象清单，使用 P1-IMG1 / P1-TXT1 / P1-CHR1 / P1-PNL1 等 ID
4. 风格与角色设定
5. 可复制到图像模型的生图 prompt
6. 如果后续只想替换烟花区域，应如何局部修改
```

局部修改示例：

```text
Use $sticker-travel-scrapbook。
这张手帐整体满意，只想把 P3-IMG2 换成我上传的真实照片。
请保留人物、标题、展品卡片、说明文字和整体版式，只给我局部修改 prompt。
```

## 本地 GUI

Skill 内置一个轻量本地 GUI，默认从空白项目开始。

启动方式：

```powershell
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

随后打开命令行中打印出的本地地址，通常是：

```text
http://127.0.0.1:8765/
```

GUI 支持旅行 brief、风格设定、素材笔记、页面和对象创建、可编辑对象 ID、当前页面 prompt 生成、项目 JSON 导入导出，以及在启用 API 后查看生成图片。

## 可选的 GUI 生图

如果启动服务器前设置了 `OPENAI_API_KEY`，GUI 可以调用 OpenAI Images API：

```powershell
$env:OPENAI_API_KEY="sk-..."
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

没有 `OPENAI_API_KEY` 时，GUI 仍然可以构建和导出 prompt；点击直接生图会显示明确的 API key 提示。

## 校验

可以用 skill creator 的校验脚本检查 Skill：

```powershell
$env:PYTHONUTF8='1'
python "C:\Users\<you>\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook"
```

期望输出：

```text
Skill is valid!
```

## 当前边界

这是一个 Skill 加本地 GUI 原型。GUI 可以构建/导出 prompt，也可以在配置 `OPENAI_API_KEY` 后直接调用 OpenAI Images API。
