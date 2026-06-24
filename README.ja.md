![Sticker Travel Scrapbook banner](assets/brand/banner.jpg)

# ステッカー旅行スクラップブック

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

`sticker-travel-scrapbook` は、東アジア風のステッカー旅行スクラップブックやミニコミック旅行日記を作成、設計、修正、対話的に編集するための Codex Skill です。

この Skill は、整った旅程表や写真集ではなく、記憶を中心にしたビジュアル制作を重視します。旅先の場面、気分、同行者、食べ物、小物、チケット風の紙片、写真スロット、ステッカー、マスキングテープ、小さな漫画的瞬間を扱います。

## サンプルギャラリー

以下は公開用に生成した安全なサンプルです。個人の旅行写真、商用キャラクター、ブランドマスコット、実在のチケット、個人の肖像は含まれていません。

<table>
  <tr>
    <td width="44%" rowspan="2" valign="top">
      <strong>縦長ページ：京都の雨の寺町</strong><br>
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

## この Skill でできること

- 旅行素材を、スクラップブックに使いやすい記憶シーンへ整理します。
- 東アジア風のステッカー構成、ミニコミック構成、ハイブリッドなコラージュ構成を設計します。
- `P1-IMG1`、`P1-TXT1`、`P1-CHR1`、`P1-STK1`、`P1-PNL1` などの安定した ID を持つ編集可能なオブジェクト一覧を作ります。
- 複数ページにわたるキャラクターとスタイルの一貫性を保ちます。
- 新規生成や局所修正に使える画像生成プロンプトを作ります。
- ページ全体を作り直さず、写真枠、ステッカー、テキストカード、漫画コマだけを差し替える指示を作れます。
- ローカル Web GUI で、プロジェクト編集、プロンプト作成、JSON のインポート/エクスポート、API 設定時の画像生成を支援します。

## リポジトリ構成

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

個人の旅行写真、キャラクター設定画、実在のチケット、ホテル情報、個人的な生成画像は公開リポジトリに入れないでください。

## インストール

このリポジトリのフォルダを Codex の skills ディレクトリにコピーし、フォルダ名を `sticker-travel-scrapbook` のままにします。

Windows では一般的に次の場所です。

```powershell
C:\Users\<you>\.codex\skills\sticker-travel-scrapbook
```

Codex がすぐに Skill を検出しない場合は、Codex を再起動するか、新しいスレッドを開始してください。

## Codex での基本的な使い方

Skill を明示的に呼び出します。

```text
Use $sticker-travel-scrapbook.
I want to create an East Asian sticker-style travel scrapbook / mini-comic page.

Trip content:
June 19, city park night visit, summer festival. Key memories include night lights, a small parade, a roller coaster, snacks, fireworks, and walking back through a lively crowd. The mood is excited, warm, and celebratory.

Please output:
1. A structured travel-memory table
2. Page format and layout suggestions
3. An editable object manifest using IDs such as P1-IMG1 / P1-TXT1 / P1-CHR1 / P1-PNL1
4. Style and character settings
5. A copyable image-generation prompt
6. A localized revision instruction for replacing only the fireworks area later
```

局所修正の例：

```text
Use $sticker-travel-scrapbook.
I like the whole scrapbook page. Only replace P3-IMG2 with my uploaded real photo.
Keep the people, title, museum cards, captions, and overall layout unchanged.
Give me only a localized revision prompt.
```

## ローカル GUI

Skill には軽量なローカル GUI が含まれています。初期状態では空のプロジェクトから開始します。

起動方法：

```powershell
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

表示されたローカル URL を開きます。通常は次の URL です。

```text
http://127.0.0.1:8765/
```

GUI では、旅行 brief、スタイル設定、素材メモ、ページとオブジェクト作成、編集可能なオブジェクト ID、現在ページのプロンプト生成、プロジェクト JSON のインポート/エクスポート、API 有効時の生成画像ギャラリーを扱えます。

## 任意の GUI 画像生成

サーバー起動前に `OPENAI_API_KEY` を設定すると、GUI から OpenAI Images API を呼び出せます。

```powershell
$env:OPENAI_API_KEY="sk-..."
python "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook\scripts\server.py" --project ".\sticker-travel-scrapbook-project.json"
```

## 検証

skill creator の検証スクリプトで Skill を確認できます。

```powershell
$env:PYTHONUTF8='1'
python "C:\Users\<you>\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "C:\Users\<you>\.codex\skills\sticker-travel-scrapbook"
```

期待される出力：

```text
Skill is valid!
```

## 現在の範囲

これは Skill とローカル GUI のプロトタイプです。GUI は Codex や別の画像ツール向けにプロンプトを作成/エクスポートできます。また、`OPENAI_API_KEY` を設定した場合は OpenAI Images API を直接呼び出せます。
