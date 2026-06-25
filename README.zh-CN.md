<p align="center">
  <img src="assets/brand/banner.jpg" alt="Trip Canvas banner">
</p>

<h1 align="center">🧳 Trip Canvas 旅行手帐 Skill</h1>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AgentSkills-Standard-8b5cf6" alt="AgentSkills Standard">
  <img src="https://img.shields.io/badge/Codex-Skill-10b981" alt="Codex Skill">
  <img src="https://img.shields.io/badge/Local-GUI-0ea5e9" alt="Local GUI">
</p>

Trip Canvas（skill id: `trip-canvas`）是一个 Codex Skill，用来创建、规划、修改和交互式编辑多风格旅行手帐页面、视觉旅行日记与小漫画旅行日记。

它的重点不是规整的旅行攻略或照片书，而是记忆优先的视觉创作：场景、情绪、同行者、食物、小物件、票据感碎片、照片槽位、贴纸、地图、拍立得、水彩、复古纸料、城市速写、黑白简笔画和小漫画瞬间。

默认情况下，它不是单纯的 prompt 生成器，而是一个由 Codex 主动推进的手帐创作流程。用户可以直接发送已经完成的旅行行程、照片、笔记和粗略偏好；Codex 会识别材料、只追问关键缺口、先草拟页面/组件/对象清单，再帮助用户生成最终手帐图、导出 prompt，或打开 GUI 进行完全手动控制。

在可用图像生成工具/API 时，Trip Canvas 还应该在规划阶段自动生成低保真版式草图和对象地图，让用户先看见页面结构，再决定是否生成最终图。

## 🖼️ 示例图集

尺寸与版式自由度示例，使用同一种可爱贴纸漫画路线：

<table>
  <tr>
    <td width="44%" rowspan="2" valign="top">
      <strong>长条手机页：京都雨天寺社街</strong><br>
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

视觉路线示例：

<table>
  <tr>
    <td width="44%" rowspan="2" valign="top">
      <strong>黑白卡通简笔画</strong><br>
      <img src="assets/examples/black-white-doodle-rainy-temple.jpg" alt="黑白卡通简笔画旅行手帐示例" width="100%">
    </td>
    <td width="56%" valign="top">
      <strong>带地图的信息图手帐</strong><br>
      <img src="assets/examples/map-infographic-coastal-train.jpg" alt="地图信息图旅行手帐示例" width="100%">
    </td>
  </tr>
  <tr>
    <td width="56%" valign="top">
      <strong>拍立得照片拼贴</strong><br>
      <img src="assets/examples/polaroid-weekend-notes.jpg" alt="拍立得照片拼贴旅行手帐示例" width="100%">
    </td>
  </tr>
</table>

## ✨ 这个 Skill 能做什么

- 引导小白用户从零散旅行材料走到具体手帐方案。
- 把旅行素材整理成适合手帐创作的记忆场景。
- 仅在风格、人物形象、布局、文字或是否生图不清楚时追问关键问题。
- 规划多风格手帐、视觉日记、小漫画和混合拼贴版式。
- 在东亚贴纸漫画、kawaii 贴纸日记、黑白卡通简笔画、地图信息图、拍立得照片拼贴、水彩旅行日记、复古纸料拼贴、城市速写、极简线描、漫画书页面、混合媒材拼贴等视觉路线中选择合适表达。
- 生成可编辑对象清单，并使用 `P1-IMG1`、`P1-TXT1`、`P1-CHR1`、`P1-STK1`、`P1-PNL1` 等稳定 ID。
- 在可用图像生成工具/API 时，自动生成低保真版式草图和可编辑对象地图。
- 在用户希望分阶段控制时，先草拟人物贴纸、照片槽位、场景分镜、文字卡、地图/票据碎片和装饰贴纸等组件。
- 维持多页之间的角色和视觉风格一致性。
- 生成可复制到图像模型中的整页 prompt、组件 prompt 或局部修改 prompt；在可用图像工具/API 支持且用户需要时，也可以继续生成图片。
- 支持只替换某个照片槽、贴纸、文字卡片或漫画分镜，而不重做整页。
- 提供本地网页 GUI，作为完全手动控制模式，用于编辑项目、生成 prompt、导入导出 JSON，以及在配置 API key 后直接生图。

## 🧩 Agent Skills 兼容性

这个仓库遵循 [Agent Skills](https://agentskills.io/) 的结构：根目录包含带 YAML frontmatter 的 `SKILL.md`，并通过可选的 `references/`、`scripts/` 和 `assets/` 目录实现渐进式加载。

当前可安装的 Skill id 是 `trip-canvas`。如果重命名文件夹，需要让文件夹名和 `SKILL.md` 里的 `name` 字段保持一致。

## 📁 仓库结构

```text
trip-canvas/
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
      black-white-doodle-rainy-temple.jpg
      kyoto-rainy-temple.jpg
      map-infographic-coastal-train.jpg
      polaroid-weekend-notes.jpg
      seoul-hanok-market.jpg
      taiwan-coastal-train.jpg
    gui/
      index.html
      blank-project.json
      demo-project.json
  references/
    authoring-workflow.md
    memory-structure.md
    scrapbook-visual-routes.md
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

## ⚙️ 安装

在 Claude Code、Codex、OpenClaw 等支持 Skill 的 Agent 里，直接说：

```text
帮我安装这个 skill：https://github.com/JAdpp/trip-canvas
```

Agent 会自己 clone 或复制到对应的 skills 目录，不用你操心路径。安装后的文件夹名请保持为 `trip-canvas`，因为 `SKILL.md` 里的 `name` 使用这个 id。

手动安装备用：把这个仓库文件夹复制到 skills 目录，并把文件夹名改成 `trip-canvas`。

Windows 用户常见位置：

```powershell
C:\Users\<you>\.codex\skills\trip-canvas
```

如果 Codex 没有立刻识别 Skill，可以重启 Codex 或开启一个新线程。

## 🚀 在 Codex 中使用

可以显式调用这个 Skill。对于小白用户，可以直接给旅行素材，让 Codex 帮你推进缺失决策：

```text
Use $trip-canvas。
我想做一张旅行手帐/视觉日记/小漫画页面，但我还不确定具体风格和布局。

旅行内容：
6 月 19 日，城市乐园夜游，夏日祭。重点记忆包括夜间灯光、小型巡游、过山车、小吃、烟花、在人群中散步返程。整体情绪是兴奋、热闹、有庆祝感。

请输出：
1. 旅行记忆结构表
2. 关键缺失问题或默认假设
3. 页面形式与版式建议，并在可用图像生成工具时生成低保真版式草图
4. 可编辑对象清单与组件草案，使用 P1-IMG1 / P1-TXT1 / P1-CHR1 / P1-PNL1 等 ID，并生成对象地图草图
5. 视觉路线、人物形象设定和精确文字清单
6. 组件 prompt 或整页生图 prompt
7. 最后问我要生成整页手帐图、先生成组件、导出 prompt pack，还是打开 GUI
```

如果风格、布局、文字、人物形象和生成目标已经很清晰，Codex 应该直接执行，不需要额外追问。

局部修改示例：

```text
Use $trip-canvas。
这张手帐整体满意，只想把 P3-IMG2 换成我上传的真实照片。
请保留人物、标题、展品卡片、说明文字和整体版式，只给我局部修改 prompt。
```

## 🛠️ 本地 GUI

Skill 内置一个用于完全手动控制的轻量本地 GUI，默认从空白项目开始。

启动方式：

```powershell
python "C:\Users\<you>\.codex\skills\trip-canvas\scripts\server.py" --project ".\trip-canvas-project.json"
```

随后打开命令行中打印出的本地地址，通常是：

```text
http://127.0.0.1:8765/
```

GUI 支持旅行 brief、风格设定、素材笔记、页面和对象创建、可编辑对象 ID、当前页面 prompt 生成、项目 JSON 导入导出，以及在启用 API 后查看生成图片。当你想自己直接控制对象和生成参数，而不是通过对话让 Codex 带着走时，使用 GUI。

## 🎨 可选的 GUI 生图

如果启动服务器前设置了 `OPENAI_API_KEY`，GUI 可以调用 OpenAI Images API：

```powershell
$env:OPENAI_API_KEY="sk-..."
python "C:\Users\<you>\.codex\skills\trip-canvas\scripts\server.py" --project ".\trip-canvas-project.json"
```

没有 `OPENAI_API_KEY` 时，GUI 仍然可以构建和导出 prompt；点击直接生图会显示明确的 API key 提示。

## 📌 当前边界

这是一个 Skill 加本地 GUI 原型。默认 Skill 行为是由 Codex 主动推进的手帐创作流程；prompt pack 和 GUI 是这个流程中的两种控制方式。是否能直接生图取决于用户当前 Codex/运行环境中可用的图像工具或 API key。

## 📄 许可证

本项目遵循 MIT 协议，详见 [LICENSE](LICENSE)。
