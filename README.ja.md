<p align="center">
  <img src="assets/brand/banner.jpg" alt="Trip Canvas banner">
</p>

<h1 align="center">🧳 Trip Canvas 旅行スクラップブック Skill</h1>

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

Trip Canvas は、`sticker-travel-scrapbook` の短いプロダクト名です。多様なスタイルの旅行スクラップブック、ビジュアル旅行ジャーナル、ミニコミック旅行日記を作成、設計、修正、対話的に編集するための Codex Skill です。

この Skill は、整った旅程表や写真集ではなく、記憶を中心にしたビジュアル制作を重視します。旅先の場面、気分、同行者、食べ物、小物、チケット風の紙片、写真スロット、ステッカー、地図、ポラロイド、水彩、ヴィンテージ紙片、都市スケッチ、白黒カートゥーン風ドゥードル、小さな漫画的瞬間を扱います。

標準では、単なるプロンプト生成器ではなく、Codex が能動的に進めるスクラップブック制作ワークフローです。ユーザーは完成した旅程、写真、メモ、大まかな好みを渡すだけでかまいません。Codex は素材を読み取り、必要な点だけ質問し、ページ/コンポーネント/オブジェクト一覧を下書きしてから、最終画像生成、プロンプト出力、または GUI での手動編集へ進めます。

## 🖼️ サンプルギャラリー

以下は公開用に生成した安全なサンプルです。個人の旅行写真、商用キャラクター、ブランドマスコット、実在のチケット、個人の肖像は含まれていません。

サイズとレイアウトの自由度の例です。同じかわいいステッカー漫画ルートを使っています。

<table>
  <tr>
    <td width="44%" rowspan="2" valign="top">
      <strong>縦長スマホページ：京都の雨の寺町</strong><br>
      <img src="assets/examples/kyoto-rainy-temple.jpg" alt="京都の雨の寺町スクラップブック例" width="100%">
    </td>
    <td width="56%" valign="top">
      <strong>単ページ：ソウルの韓屋村と夜市</strong><br>
      <img src="assets/examples/seoul-hanok-market.jpg" alt="ソウル韓屋村と夜市スクラップブック例" width="100%">
    </td>
  </tr>
  <tr>
    <td width="56%" valign="top">
      <strong>見開き：台湾の海沿い列車とランタンの旧市街</strong><br>
      <img src="assets/examples/taiwan-coastal-train.jpg" alt="台湾海沿い列車スクラップブック例" width="100%">
    </td>
  </tr>
</table>

ビジュアルルートの例：

<table>
  <tr>
    <td width="44%" rowspan="2" valign="top">
      <strong>白黒カートゥーン風ドゥードル</strong><br>
      <img src="assets/examples/black-white-doodle-rainy-temple.jpg" alt="白黒カートゥーン風ドゥードルの旅行スクラップブック例" width="100%">
    </td>
    <td width="56%" valign="top">
      <strong>地図つき情報グラフィック手帳</strong><br>
      <img src="assets/examples/map-infographic-coastal-train.jpg" alt="地図情報グラフィックの旅行スクラップブック例" width="100%">
    </td>
  </tr>
  <tr>
    <td width="56%" valign="top">
      <strong>ポラロイド写真コラージュ</strong><br>
      <img src="assets/examples/polaroid-weekend-notes.jpg" alt="ポラロイド写真コラージュの旅行スクラップブック例" width="100%">
    </td>
  </tr>
</table>

## ✨ この Skill でできること

- 初心者ユーザーを、散らばった旅行素材から具体的なスクラップブック案へ案内します。
- 旅行素材を、スクラップブックに使いやすい記憶シーンへ整理します。
- スタイル、人物像、レイアウト、文字、画像生成の意図が不明な場合だけ、重要な質問を絞って行います。
- 多様なスタイルのスクラップブック、ビジュアルジャーナル、ミニコミック、ハイブリッドなコラージュ構成を設計します。
- 東アジア風ステッカー漫画、kawaii ステッカージャーナル、白黒カートゥーン風ドゥードル、地図情報グラフィック、ポラロイド写真コラージュ、水彩旅行ジャーナル、ヴィンテージ紙片スクラップブック、都市スケッチ、ミニマル線画、コミックブック風ページ、ミクストメディアコラージュなどのビジュアルルートを選べます。
- `P1-IMG1`、`P1-TXT1`、`P1-CHR1`、`P1-STK1`、`P1-PNL1` などの安定した ID を持つ編集可能なオブジェクト一覧を作ります。
- 段階的に確認したい場合は、人物ステッカー、写真スロット、場面パネル、テキストカード、地図/チケット片、装飾ステッカーなどのコンポーネント案を先に作ります。
- 複数ページにわたるキャラクターとスタイルの一貫性を保ちます。
- 全体ページ用プロンプト、コンポーネント用プロンプト、局所修正プロンプトを作ります。画像生成ツール/API が利用可能で、ユーザーが望む場合は画像生成まで進めます。
- ページ全体を作り直さず、写真枠、ステッカー、テキストカード、漫画コマだけを差し替える指示を作れます。
- ローカル Web GUI を、プロジェクト編集、プロンプト作成、JSON のインポート/エクスポート、API 設定時の画像生成を行う手動コントロールモードとして提供します。

## 🧩 Agent Skills 互換性

このリポジトリは [Agent Skills](https://agentskills.io/) の構造に沿っています。ルートに YAML frontmatter 付きの `SKILL.md` を置き、必要に応じて `references/`、`scripts/`、`assets/` を使って段階的に情報を読み込めるようにしています。

インストール可能な Skill id は引き続き `sticker-travel-scrapbook` です。フォルダ名を変更する場合は、フォルダ名と `SKILL.md` の `name` フィールドを一致させてください。

## 📁 リポジトリ構成

```text
sticker-travel-scrapbook/
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

個人の旅行写真、キャラクター設定画、実在のチケット、ホテル情報、個人的な生成画像は公開リポジトリに入れないでください。

## ⚙️ インストール

Claude Code、Codex、OpenClaw など Skill に対応した Agent で、次のように伝えてください。

```text
Install this skill:
https://github.com/JAdpp/Sticker-Travel-Scrapbook-Skill
Please install it as the skill folder named sticker-travel-scrapbook.
```

Agent が環境に合った skills ディレクトリへ clone またはコピーします。インストール後のフォルダ名は `sticker-travel-scrapbook` のままにしてください。`SKILL.md` の `name` がこの id を使っているためです。

手動で入れる場合は、このリポジトリのフォルダを skills ディレクトリにコピーし、フォルダ名を `sticker-travel-scrapbook` にします。

Windows では一般的に次の場所です。

```powershell
C:\Users\<you>\.codex\skills\sticker-travel-scrapbook
```

Codex がすぐに Skill を検出しない場合は、Codex を再起動するか、新しいスレッドを開始してください。

## 🚀 Codex での基本的な使い方

Skill を明示的に呼び出します。初心者向けには、旅行素材を渡して Codex に不足している判断を進めてもらえます。

```text
Use $sticker-travel-scrapbook.
I want to create a travel scrapbook / visual journal / mini-comic page, but I am not sure about the exact style and layout yet.

Trip content:
June 19, city park night visit, summer festival. Key memories include night lights, a small parade, a roller coaster, snacks, fireworks, and walking back through a lively crowd. The mood is excited, warm, and celebratory.

Please output:
1. A structured travel-memory table
2. Any key missing questions or default assumptions
3. Page format and layout suggestions
4. An editable object manifest and component draft using IDs such as P1-IMG1 / P1-TXT1 / P1-CHR1 / P1-PNL1
5. Visual route, character/persona settings, and exact text list
6. Component prompts or a final image-generation prompt
7. Ask me whether to generate the final scrapbook image, generate components first, export the prompt pack, or open the GUI
```

スタイル、レイアウト、文字、人物像、生成目標がすでに明確な場合、Codex は余計な質問をせずに直接進めるべきです。

局所修正の例：

```text
Use $sticker-travel-scrapbook.
I like the whole scrapbook page. Only replace P3-IMG2 with my uploaded real photo.
Keep the people, title, museum cards, captions, and overall layout unchanged.
Give me only a localized revision prompt.
```

## 🛠️ ローカル GUI

Skill には、完全に手動で制御するための軽量なローカル GUI が含まれています。初期状態では空のプロジェクトから開始します。

起動方法：

```powershell
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

表示されたローカル URL を開きます。通常は次の URL です。

```text
http://127.0.0.1:8765/
```

GUI では、旅行 brief、スタイル設定、素材メモ、ページとオブジェクト作成、編集可能なオブジェクト ID、現在ページのプロンプト生成、プロジェクト JSON のインポート/エクスポート、API 有効時の生成画像ギャラリーを扱えます。Codex との対話で進めるより、自分でオブジェクトや生成設定を直接制御したい場合に使います。

## 🎨 任意の GUI 画像生成

サーバー起動前に `OPENAI_API_KEY` を設定すると、GUI から OpenAI Images API を呼び出せます。

```powershell
$env:OPENAI_API_KEY="sk-..."
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

## ✅ 検証

skill creator の検証スクリプトで Skill を確認できます。

```powershell
$env:PYTHONUTF8='1'
python "C:\Users\<you>\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook"
```

期待される出力：

```text
Skill is valid!
```

Agent Skills の公式リファレンス検証ツールをインストールしている場合は、次のようにも確認できます。

```bash
skills-ref validate ./sticker-travel-scrapbook
```

## 📌 現在の範囲

これは Skill とローカル GUI のプロトタイプです。標準の Skill 動作は、Codex が能動的に進めるスクラップブック制作ワークフローです。プロンプトパックと GUI は、そのワークフロー内の二つのコントロール方法です。直接画像生成できるかどうかは、ユーザーの Codex/実行環境で利用できる画像ツールまたは API key に依存します。
