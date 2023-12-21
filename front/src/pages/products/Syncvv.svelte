<script>
	import hero from '../../assets/products/syncvv/banner.jpg';
	import image1 from '../../assets/products/syncvv/system-picture-1.png';
	import image2 from '../../assets/products/syncvv/vicon-rec-trigger.png';
	import image3 from '../../assets/products/syncvv/system-block-diagram.png';
	import image4 from '../../assets/products/syncvv/bluefish444.png';
	import image5 from '../../assets/products/syncvv/channel-expansion.png';
	import image6 from '../../assets/products/syncvv/high-quality-encoder.png';
	import image7 from '../../assets/products/syncvv/various-video-formats.jpg';
	import image8 from '../../assets/products/syncvv/timecode-rec-trigger.png';
	import image9 from '../../assets/products/syncvv/userinterface.png';
	import image10 from '../../assets/products/syncvv/cms.png';
	import image11 from '../../assets/products/syncvv/rating.png';
	import image12 from '../../assets/products/syncvv/tags-notes-description.png';
	import image13 from '../../assets/products/syncvv/takelist-thumbnail.png';
	import image14 from '../../assets/products/syncvv/still-image-capture.png';
	import image15 from '../../assets/products/syncvv/export-take-footage.gif';
	import image16 from '../../assets/products/syncvv/search.png';
	import image17 from '../../assets/products/syncvv/timecode.png';
	import image18 from '../../assets/products/syncvv/textinserter.png';
	import image19 from '../../assets/products/syncvv/osd.webp';
	import image20 from '../../assets/products/syncvv/rotate.webp';
	import image21 from '../../assets/products/syncvv/large-view-window.png';
	import image22 from '../../assets/products/syncvv/shortcutkeys.png';
	import image23 from '../../assets/products/syncvv/streamdeck.png';
	import image24 from '../../assets/products/syncvv/builtindocuments.png';
	import image25 from '../../assets/products/syncvv/local-audio-monitor.png';
	import image26 from '../../assets/products/syncvv/audio-waveform-display.png';
	import image27 from '../../assets/products/syncvv/system-monitor.png';
	import image28 from '../../assets/products/syncvv/broken-channel-signal.png';
	import image29 from '../../assets/products/syncvv/sha-256.png';
	import image31 from '../../assets/products/syncvv/takelist-microsoft-excel.png';
	import image32 from '../../assets/products/syncvv/takelist-google-sheets.png';
	import image33 from '../../assets/products/syncvv/directory-structure.png';
	import image34 from '../../assets/products/syncvv/json.png';
	import image35 from '../../assets/products/syncvv/cloud-service.png';
	import image36 from '../../assets/products/syncvv/realtimesystemtechnologies.png';
	import image37 from '../../assets/products/syncvv/feedback.png';
	import { onMount } from 'svelte';

	let isFixedNav = false;
	let activeSection = null;

	onMount(async () => {
		window.scrollTo(0, 0);
		const heroHeight = document.querySelector('.hero');
		const sidebarItems = document.querySelectorAll('.sidebar-item');
		const sections = document.querySelectorAll('.content > section');

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting && entry.intersectionRatio >= 0.1) {
						const targetId = entry.target.id;
						activeSection = targetId;
						sidebarItems.forEach((item) => {
							if (item.getAttribute('href') === `#${targetId}`) {
								item.classList.add('active');
							} else {
								item.classList.remove('active');
							}
						});
					}
				});
			},
			{ threshold: 0.1 }
		);

		sections.forEach((section) => {
			observer.observe(section);
		});

		window.addEventListener('scroll', () => {
			const scrollPosition = window.scrollY || document.documentElement.scrollTop;
			isFixedNav = scrollPosition >= heroHeight.offsetHeight;
		});
	});

	function scrollToElement(event) {
		event.preventDefault();

		const targetId = event.target.hash.substr(1);
		const targetElement = document.getElementById(targetId);

		if (targetElement) {
			targetElement.scrollIntoView({ behavior: 'smooth' });
		}
	}
</script>

<div class="pageContent">
	<div class="hero">
		<h1>SyncVV II</h1>
		<figure class="hero-image-container">
			<img class="hero-image" src={hero} alt="4d studios" />
		</figure>
	</div>

	<div class={isFixedNav ? 'sidebar sidebar-fixed' : 'sidebar'}>
		<a class="sidebar-item active" href="#overview" on:click={scrollToElement}>概要</a>
		<a class="sidebar-item" href="#specs" on:click={scrollToElement}>特徴</a>
		<a class="sidebar-item" href="#support" on:click={scrollToElement}>サポート</a>
		<!-- <a class="sidebar-item" href="#contact" on:click={scrollToElement}>お問い合わせ</a> -->
	</div>

	<div class="content">
		<section class="overview" id="overview">
			<div class="container">
				<h3>概要</h3>
				<p class="explanation">
					初代SyncVV
					から大幅に機能強化し、収録作業だけでなくポストプロダクション作業を含めて運用負荷を軽減します
				</p>
				<figure>
					<img alt="" src={image1} />
				</figure>
				<p class="explanation">
					SyncVVII は、4 系統のSDI
					入力を備えた業務用映像音声収録システムです。高度に統合化されたソフトウェアアーキテクチャにより、撮影からポストプロダクションまでをシームレスに接続。新たに追加された素材管理システムにより、収録現場の大幅な省力化が可能になりました。10
					年続いた初代SyncVV のDNA を受け継ぎ、新しく 撮影していることを忘れさせる撮影ソリューション
					として生まれ変わったSyncVV II は、次の時代の収録システムを実現します。
				</p>

				<iframe
					frameborder="0"
					height="400px"
					src="https://player.vimeo.com/video/867536797?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
					style="width:100%;"
					title="Tether Video"
					width="400px"
				></iframe>
			</div>

			<!-- <ul class="features-list">
					<li class="features-list-item">
						アダプティブビットレートのサポートによりLTE・WIFIなど回線速度に応じて最適なクオリティで視聴が可能
					</li>
					<li class="features-list-item">ダウンロードの要らないコンテンツ体験</li>
					<li class="features-list-item">Unity, Unreal, Webへのストリーミング用API</li>
					<li class="features-list-item">マーカーレスARソフト：8th WALLとのインテグレーション</li>
				</ul> -->
		</section>

		<section class="specs" id="specs">
			<div class="container">
				<h2>特徴</h2>

				<h3>Viconシステムと連動した自動収録</h3>
				<p class="explanation-big">
					進化したVicon システム連動自動収録機能は、現場作業負荷を大幅に低減しました。
				</p>

				<details>
					<summary>Vicon システムと連動した自動収録に対応</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image2} style="float:left" /></p>

						<p>
							Viconシステムと連動した自動収録機能は、SyncVV-IIシステムの操作負荷を大幅に低減します。
							Viconシステムの収録開始信号を受信したSyncVV-IIは、自動的にテイク情報を取得。
							プロジェクトへのテイク登録から収録開始と収録終了までを完全自動化できます。
							数多くの機材が並ぶ収録現場において、機材オペレーションにかかる負荷は日々高まるばかりですが、SyncVV-IIに搭載されたViconシステム連動自動収録機能は、現場作業負荷を大幅に低減します。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>柔軟な入力ソース</h3>
				<p class="explanation-big">従来どおりの4 チャネルSDI 入力は非同期信号にも対応しました。</p>

				<details>
					<summary>4チャネル同期 非同期SDI 信号収録システム</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image3} style="float:left" /></p>

						<p>
							SyncVV-IIは、同期した4チャネルSDI信号の収録はもちろんのこと、異なるビデオフォーマットを組み合わせた非同期4チャネルSDI信号の収録にも対応しました。
							1台のシステムで異なるビデオフォーマットに柔軟に対応することで、システム全体コストを大幅に低減。
							入力した映像はmp4コンテナに入った映像素材ファイルにリアルタイムエンコードされ、即座にポストプロダクションで使用可能な映像素材に変換されます。
						</p>
					</div>
				</details>

				<details>
					<summary>高信頼性SDI 入力カード採用</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image4} style="float:left" /></p>

						<p>
							SyncVV-IIのSDI入力には、高い信頼性を誇るBluefish Technologies社のSupernova S+を採用。
							広帯域性能を安定して得る基幹技術群には、業界における長年の経験から得られた数多くの知見が活かされています。
							Bluefish444の無制限保証と極めて低いRMA率は、米軍がITハードウェア製造に要求するのと同じ厳しい基準を満たす工業用製造工程によって実現されています。
							組み立て工程は、政府機関による監査で定期的に検証され、ISO9001の認定を受けています。
							業務用機器には業務用コンポーネントを。 SyncVVのこだわりのひとつです。
						</p>
					</div>
				</details>

				<details>
					<summary>複数台並列稼働によるチャネル拡張</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image5} style="float:left" /></p>

						<p>
							近年、Viconシステムを使った撮影環境は大規模化の一途をたどっています。
							精細感溢れる映像表現を創り出す撮影環境において、制作支援のための映像収録環境も拡張が欠かせません。
							SyncVVシステムは、複数台並列稼働によるチャネル数の拡張にも対応。
							Viconシステムからブロードキャストされる収録トリガー信号を使って、複数のSyncVVシステムを連動制御できます。
							ハウスシンクと同期した適切なタイムコードを入力することで、頭のフレームが完全に揃う同期収録制御を新たに開発。
							ポストプロダクションにおいても煩雑な頭合わせのような作業が一切不要の高効率ワークフローを構築できます。
						</p>
					</div>
				</details>

				<details>
					<summary>業務用高品質SDI リアルタイムエンコーダ搭載</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image6} style="float:left" /></p>

						<p>
							4系統のSDI信号を同時入力するシステムにおいて、優れたリアルタイム性を持つエンコーダの存在は非常に重要です。
							SyncVV-IIでは、基幹設計に業務用高品質リアルタイムエンコーダを搭載。
							ベースバンドSDI信号を広帯域で取り込みながら、同時に映像と音声のリアルタイムエンコードを4系統並列で実行する能力を兼ね備えました。
							この高いリアルタイム性と高品質な映像を実現する基本設計により、ミッションクリティカルな収録業務を強力にサポート。
							業務用ビデオからポストプロダクションまでを一気通貫で接続する、新しい映像メディアシステムが誕生しました。
						</p>
					</div>
				</details>

				<details>
					<summary>豊富な入力ビデオフォーマット</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image7} style="float:left" /></p>

						<p>
							SyncVV-IIは、様々な入力ビデオフォーマットに対応することで、現場で映像機器を選定する負荷を大幅に低減します。
							対応ビデオフォーマットは、2048x1080プログレッシブの場合に60pから23.98p、1920x1080プログレッシブの場合に60pから23.98p、1920x1080インターレースの場合に60iから50i。
							1280x720は60pから23.98pまでと、幅広い入力ビデオフォーマットに対応。
							プログレッシブセグメンテッドフレームにも対応し、様々な映像機器が接続される現場でも安心して御利用頂けます。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>効率的な収録作業を実現する操作性の向上</h3>
				<p class="explanation-big">タイムコードを活用した制御命令や画面構成。</p>

				<details>
					<summary>タイムコード収録開始指令と収録終了指令</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image8} style="float:left" /></p>

						<p>
							SyncVV-IIに接続したSDI信号にVITCやLTCを重畳し、予め定義されたタイムコード収録開始指令と収録終了指令を使うことで、収録素材の先頭フレームと最終フレームを完全に一致させることが可能になりました。
							従来型ソフトウェアベース収録システムでは考えられなかった完全同期収録制御システムを実現。
							ポストプロダクションにおける頭合わせの作業が一切不要となり、大規模化するワークフローの作業効率を格段に向上させます。
							もちろんViconシステムからの収録開始指令と収録終了指令でも使用可能。
							多段に複数のビデオ装置が接続されるモーションキャプチャ完全自動化収録システムにおける素材の完全性に配慮しました。
						</p>
					</div>
				</details>

				<details>
					<summary>状況を一目で確認できるトランスポートコントロール画面</summary>
					<div>
						<br />
						<p>
							様々な情報を瞬時に確認しなければならない撮影現場において、状況を一目で確認する手段の存在は極めて重要です。
							SyncVV-IIのトランスポートコントロール画面は、タイムコード表示、オーディオ波形モニタ、オーディオレベルメータ、収録対象プロジェクト、収録テイク数と統計情報を凝縮した画面で一括表示。
							視線をあちこち移動させることなくシステムの状況を一目で確認できるので安心です。
						</p>
						<br />
						<p>
							<img
								alt=""
								src="/media/uploads/2023/12/18/transport-control.png"
								style="float:left"
							/>
						</p>
					</div>
				</details>

				<details>
					<summary>撮影現場のニーズを熟知した画面レイアウト</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image9} style="float:left" /></p>

						<p>
							慌ただしく膨大な作業を求められる収録現場において、分かりやすい画面レイアウトは極めて重要。
							SyncVV-IIの直感的に状況を把握できる画面レイアウトは、撮影現場のニーズを熟知したエンジニアリングチームによって生まれました。
							薄暗い撮影現場でも環境に馴染む黒基調の画面に、操作用コンポーネントを独自の基準で整理して配置。
							左側から入力、中央に撮影済み素材、右側に撮影済み素材のサムネイルを表示する構成により、直感的に状況を把握できるようになりました。
							この直感的な画面レイアウトにより、収録現場の作業負荷を大幅に低減します。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>撮影素材を効率的に管理する素材管理システムを装備しました</h3>
				<p class="explanation-big">
					大量のテイクを効率的に把握し、格付け・分類して収録後即座にポストプロセスに撮影素材を引き渡すためのツールを提供しました。
				</p>

				<details>
					<summary>撮影素材を効率的に管理する素材管理システム</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image10} style="float:left" /></p>

						<p>
							慌ただしい現場では、1日の収録が完了した瞬間から即座にポストプロセスへの素材搬入を開始したいもの。
							SyncVV-IIでは、撮影素材を効率的に管理する新しい素材管理システムを搭載。
							直交性のある見やすいテイクリストは、テイクが持つ多様なパラメータをひと目で確認するのに役立ちます。
							各テイクにお好みの色を付けて管理可能な機能は、数多くの機材を操作しなければならない収録現場において視認性を向上させるもの。
							人間工学に配慮した数々のユニークな工夫によって、システム導入直後からスムースなオペレーションをお約束します。
						</p>
					</div>
				</details>

				<details>
					<summary>テイクのレイティング</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image11} style="float:left" /></p>

						<p>
							大量の素材が生み出される撮影現場では、数分前のテイクがどのような状態だったのか把握するのも一苦労。
							デジタル機材を運用している時にノートでメモを取るような対応を迫られる事さえ起こり得ます。
							新しいSyncVV-IIでは、収録済みテイクに対するレイティングによって、簡単な分類が可能になりました。
							ポストプロダクションで使用する予定の素材にはOK、明らかに使わない素材にはNGなど、シンプルでありながら必要十分なレイティング機能により、スムースな現場運営を実現します。
							レイティングは見やすいアイコンで一目瞭然。新たに搭載された検索システムを使用する事で特定のレイティングのテイクのみを列挙する事も可能です。
						</p>
					</div>
				</details>

				<details>
					<summary>プロジェクトメタデータ</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image12} style="float:left" /></p>

						<p>
							SyncVV-IIでは、テイクにタグ、ノート、詳細説明の記述が可能になりました。
							テイク収録中にも編集操作が可能なため、撮影時間の合間を使った効率的なオペレーションが可能。
							タグとノートと詳細説明の使い方は、プロジェクトに併せてユーザーが選択可能です。
							また、公開されるプロジェクトファイル情報を活用する事で、ポストプロダクションに向けたワークフローの自動化にも貢献します。
							プロジェクトメタデータは、撮影現場で刻々と生まれる素材情報をシームレスにポストプロダクションに受け渡す非常に重要な役目を果たします。
						</p>
					</div>
				</details>

				<details>
					<summary>収録素材サムネイル表示機能</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image13} style="float:left" /></p>

						<p>
							SyncVV-IIのテイクリストにおいて、収録素材を直感的に把握できる収録素材サムネイル表示機能が新たに追加されました。
							数多くの収録を行なう撮影現場では、作業に応じて様々な確認手段が用意されていることが非常に重要。
							SyncVV-IIの収録素材のサムネイル表示機能は、収録済み素材の分類やメタデータ付与に欠かせない確認作業の省力化に貢献します。
							テイクリストの上部にあるスライダーを左右に動かすことで、テイクリストの表示サイズを動的に変更可能。
							確認作業の内容に応じた表示サイズをお好みで選択頂けます。
						</p>
					</div>
				</details>

				<details>
					<summary>静止画キャプチャ機能</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image14} style="float:left" /></p>

						<p>
							映像の収録とは別に、「この場面を静止画で残したい」という場面に遭遇することは少なくありません。
							SyncVV-IIに新たに搭載された静止画キャプチャ機能を用いると、ワンクリックで簡単に入力映像を静止画に保存できます。
							保存した静止画はそのままテイクリストに収録素材として管理可能。
							撮影風景やカチンコの撮影など、1フレームさえあれば良い場面で重宝します。
						</p>
					</div>
				</details>

				<details>
					<summary>必要な撮影素材をまとめてエクスポート</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image15} style="float:left" /></p>

						<p>
							SyncVV-IIでは、撮影済みテイクを簡単にポストプロダクションに渡すためのエクスポート機能を新たに搭載しました。
							これまで手動で行っていた撮影素材のファイルバックアップ操作は一切不要。
							ポストプロダクション工程への素材渡しがこれまで以上に手軽になりました。
							撮影済みテイクリストからエクスポート対象の絞り込みも可能。
							対象フィールドとキーワードを入力してリアルタイム絞り込み検索を行ない、検索結果に表示されたテイクの素材ファイルのみを外部ストレージにコピーできます。
							敏速なエクスポート機能により、撮影ワークフロー全体の効率を大幅に向上させます。
						</p>
					</div>
				</details>

				<details>
					<summary>リアルタイム絞り込み表示を可能にしたフィルタリング機能</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image16} style="float:left" /></p>

						<p>
							膨大なテイクが生まれることは問題ではなく、膨大な量のテイクに対して、成す術が無い事が問題だったのです。
							SyncVV-IIに新たに搭載された絞り込み表示を可能にするフィルタリング機能は、キーワードを入力するだけで即座に該当のテイクのみが列挙表示される敏速なユーザーインターフェースを採用。
							フィルタリング対象は自由に選択でき、収録素材に付けたタグや収録時刻など、多様なテイク情報の中から柔軟な検索操作を可能にします。
							SyncVV-IIに搭載された強力なフィルタリング機能は、従来の業務用収録システムの概念を覆すパワフルな機能です。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>高機能タイムコードジェネレータ内蔵</h3>
				<p class="explanation-big">
					多機能なタイムコードジェネレータ／リーダーを内蔵することによりファイルベースの映像のハンドリングが飛躍的に向上しました。
				</p>

				<details>
					<summary>タイムコードはVITC/LTC/External LTC に対応</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image17} style="float:left" /></p>

						<p>
							SyncVV-IIシステムでは、VITC/LTC/External LTCの3種類のタイムコードに対応。
							チャネル毎のタイムコード情報を使用したい場合にはVITC/LTC、システムグローバルなタイムコード情報を使用したい場合にはExternal
							LTCと、柔軟にタイムコードソースを選択できます。
							システムタイムコードは、チャネルA～チャネルDの中から任意のチャネルをタイムコードソースとして選択可能。
							システム構成に合わせて柔軟に運用可能なシステムを構築できます。
						</p>
					</div>
				</details>

				<details>
					<summary>撮影素材へのタイムコード焼き込み機能</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image18} style="float:left" /></p>

						<p>
							SDIのような業務用映像音声インターフェースの映像が、mp4ファイルのように汎用ファイルフォーマットになった時点で、タイムコード情報の取り扱いが極端に難しくなります。
							複数のチャネルの撮影素材の時間軸を管理する際、メタ情報だけではポストプロセスが難しくなることもしばしば。
							この場合、SyncVV-IIに搭載された撮影素材へのタイムコード焼き込み機能を用いることで、ポストプロダクションでの取り扱いを改善できます。
							タイムコード焼き込み機能は、収録対象映像がシステムに入力された時にリアルタイムにビデオフレーム内にオーバーレイされる特別な機能。
							1フレームずつタイムコード値が焼き込まれるため、収録対象素材に現れる大切な一瞬を逃しません。
						</p>
					</div>
				</details>

				<details>
					<summary>タイムコード焼き込み位置と大きさ可変</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image19} style="float:left" /></p>

						<p>
							撮影素材へのタイムコード焼き込み位置は非常に重要。
							プロジェクトをハンドリングする撮影監督や撮影対象素材によっても大きく変化します。
							SyncVV-IIでは、タイムコード表示位置を9箇所から選択可能。
							用途に合わせた表示位置をお好みでお使い頂けます。
							タイムコードの大きさは1ピクセル単位での調整が可能。
							最小サイズはタイムコード表示時に66x8ピクセルと、撮影素材を邪魔しない形でバーンイン可能。
							焼き込み設定はチャネル毎に設定でき、システム構成やプロジェクトの内容に応じた運用を実現します。
							従来は専用ハードウェアが必要だった内容をSyncVV-IIでは見事にソフトウェアで実現しました。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>操作性を向上するための機能</h3>
				<p class="explanation-big">オペレーターの負荷を軽減し、ミスを防ぐ仕組みです。</p>

				<details>
					<summary>プレビュー画面の映像回転機能</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image20} style="float:left" /></p>

						<p>
							モーションキャプチャシステムと同時に使われることの多いSyncVV-IIシステムには、通常とは異なる方向に取り付けられたカメラの映像が入力されることも少なくありません。
							SyncVV-IIに搭載されたプレビュー画面の映像回転機能を使うと、カメラを横方向に設置した場合でも、素材の方向に合わせた画面で入力映像を確認できます。
							回転の設定は、マウスの簡単な操作で即座に反映される方式を採用。
							回転なし、90度回転、180度回転、270度回転の4種類から選択できます。
							これまで顔を傾けて確認していた撮影素材も、ストレスなく短い時間で確認できるようになりました。
						</p>
					</div>
				</details>

				<details>
					<summary>ラージビューダイアログ機能の搭載</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image21} style="float:left" /></p>

						<p>
							SyncVV-IIでは、SDI入力映像のプレビューを手軽に実現するラージビューダイアログ機能を搭載しました。
							このラージビューダイアログ機能は、SyncVV-IIシステムに接続された拡張ディスプレイに映像を表示する事を想定。
							主操作画面の「ラージビュー」ボタンをクリックするだけで、画面のどこにでも配置可能なラージビューダイアログが表示されます。
							オペレータは主操作画面を見ながら操作し、撮影ディレクターはラージビューダイアログの映像を見て確認するなど、柔軟な運用体制を構築できます。
							ラージビューダイアログには、チャネルA～チャネルDまでの全4チャネルの映像を同時に表示。
							見やすいタイル型の配置により、撮影スタジオ全体の様子を即座に確認する事も可能です。
						</p>
					</div>
				</details>

				<details>
					<summary>ショートカットキーに対応</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image22} style="float:left" /></p>

						<p>
							業務用映像音声機器には、機敏な動作を可能にするインターフェースも必要不可欠です。
							SyncVV-IIでは、操作を敏速に行なうショートカットキー操作に対応しました。
							テイクへのレイティング設定、収録済み素材ファイルのコンピュータ上での再生など、多様な操作をショートカットキーのみで実現できます。
						</p>
					</div>
				</details>

				<details>
					<summary>Elgato社のStream Deck デバイスに対応</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image23} style="float:left" /></p>

						<p>
							SyncVV-IIの操作を極限まで簡単にするためのElgato Stream Deckサポートが登場しました。
							キーボードの横に配置した専用操作デバイスを使って、ワンタッチで所望の操作を実現できます。
							テイクリストの選択テイクを上下移動してテイクのレイティングを変更するのもワンプッシュで楽々。
							収録済み映像素材の再生も対象チャネルのボタンを押すだけで簡単に実行できます。
							収録開始と収録停止を手動で行ないたい場合でも簡単。
							キーボードショートカットとは異なる次元の直感的な操作環境を実現できます。
						</p>
					</div>
				</details>

				<details>
					<summary>操作系ドキュメントのビルトイン</summary>
					<div class="dynamic-image-text-flexbox">
						<p>
							<img alt="" src={image24} style="float:left" />
						</p>

						<p>
							SyncVV-IIには、ビルトインされたドキュメントが同梱されています。
							インターネットに接続されていないオフライン環境でも、ブラウザーを用いたドキュメントの閲覧が可能。
							システムやソフトウェアの詳細情報を、簡単に便利に閲覧できる環境を御用意しました。
							撮影や機材メインテナンスの合間の少しの時間を使って、システムをより便利に安心して使いこなすための情報が得られる充実した環境を御用意。
							数多くのシステムが稼働する収録現場では、少しの手間の違いが積み重なって大きな手間の違いとなるもの。
							細かな配慮や機能を知ることで、作業負荷を低減する仕組みづくりにも配慮しています。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>オーディオ部の改善</h3>
				<p class="explanation-big">
					エンベデットオーディオのモニタリング機能を内蔵し、外部オーディオ機器を不要にしてセティングタイム短縮・省スペース・コストパフォーマンスを向上させました。
				</p>

				<details>
					<summary>エンベデッドオーディオモニタリング</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image25} style="float:left" /></p>

						<p>
							SyncVV-IIのエンベデッドオーディオモニタリング機能は、システムオーディオ出力から音声を出力する機能です。
							これまで専用ハードウェアを用意していたエンベデッドオーディオのモニタリング環境を簡単に実現。
							システム全体のコストパフォーマンスを大幅に向上させます。
							モニタリング対象のチャネルは任意に選択可能。
							収録中の音声出力を抑制するためのミュート機能も搭載しました。
						</p>
					</div>
				</details>

				<details>
					<summary>見やすいオーディオ波形表示</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image26} style="float:left" /></p>

						<p>
							SyncVV-IIに搭載された見やすいオーディオ波形表示は、縦方向に流れる音声波形表示方式を採用しました。
							短い時間尺で多数の映像素材を収録する撮影現場では、映像と音声の先頭フレームと最終フレームの確認が欠かせません。
							見やすいオーディオ波形表示は、素材の完全性を収録中に確認する際に役立つ便利な機能です。
							また、SDIエンベデッドオーディオの確認を、音声出力なしで直感的に確認できることから、静粛性が求められるような撮影現場にも最適。
							新たな次元の直感的なオーディオ確認手段により、収録操作の確認負荷を低減します。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>トラブル回避策</h3>
				<p class="explanation-big">トラブルの予防、把握をサポートする機能を備えました。</p>

				<details>
					<summary>システム状態の把握</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image27} style="float:left" /></p>

						<p>
							SyncVV-IIでは、システム状態の把握を的確に行うためのシステムモニター機能を配備しました。
							収録画面のトランスポートコントロール部において、CPU稼働率、GPU稼働率を簡潔なグラフで表示。
							ハードウェアコンポーネントだけでなく、オペレーティングシステム、デバイスドライバー、アプリケーションと様々な条件が変化する現代のソフトウェア環境における状態確認の手間を大幅に低減します。
						</p>
					</div>
				</details>

				<details>
					<summary>SDI回線トラブルへの対策</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image28} style="float:left" /></p>

						<p>
							様々な機材が一時的に設置される収録現場では、SDI回線のトラブルはつきもの。
							SyncVV-IIでは、収録中にSDI回線に不具合があった場合でも、収録処理を停止しない安全機構を搭載しました。
							無効判定されたビデオフレームは破棄されますが、収録はそのまま継続。
							SDI回線が復帰した時点から映像と音声の収録が継続されます。
						</p>
					</div>
				</details>

				<details>
					<summary>SHA-256 を使った一貫性検証</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image29} style="float:left" /></p>

						<p>
							SyncVV-IIでは、重要な素材ファイルのコピー処理にも徹底したこだわりを発揮。
							ファイルシステムやディスクシステムで稀に発生する予期せぬトラブルを未然に防止する機能として、SHA-256を使った一貫性検証機能を搭載しました。
							コピー処理実行後にSHA-256ハッシュ値を使い、コピー元ファイルとコピー先ファイルの同一性検証を実行。
							SyncVV-IIは、ワークフローで使用する様々な機器や環境の事情にも配慮し、徹底した安全性を実現します。
						</p>
					</div>
				</details>

				<details>
					<summary>コンポジットガイド</summary>
					<div class="dynamic-image-text-flexbox">
						<p>
							<iframe
								src="https://player.vimeo.com/video/859986909?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
								frameborder="0"
								allow="autoplay; fullscreen; picture-in-picture"
								title="Composite Guide"
								loading="lazy"
								class="dynamic-iframe"
							>
							</iframe>
						</p>

						<p>
							モーションキャプチャーやCG合成素材を撮影する現場では、ポストプロダクション工程で必要とされる素材が撮影できているのかをオンセットで確認する事が求められます。
							特に頻繁に起こるのが、前後のテイクとの関係が期待するものになっているのか確認する作業。
							実際に撮影した複数のテイクを、記憶に頼って素材の適合性を確認するのは至難の業です。
							コンポジットガイドを使用すると、過去テイクのサムネイル画像を現在の入力映像に重ねて透過表示。
							透過濃度もスライダーで自由に設定できるので、最適な環境でカメラ入力映像を確認できます。
							また、テイクとテイクの比較表示も可能になっているため、撮影素材の前後テイクで場面に矛盾が無いかの確認にも使用できます。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>全体のワークフロー向上を見据えた仕組み</h3>
				<p class="explanation-big">
					ポストプロダクション以降のワークフローをサポートする機能を備えました。
				</p>

				<details>
					<summary>テイクリストのMicrosoft Excel 形式エクスポート</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image31} style="float:left" /></p>

						<p>
							SyncVV-IIでは、収録映像素材管理のワークフローを劇的に省力化するために、テイクリストをMicrosoft
							Excel形式(拡張子xlsx)で書き出せるエクスポート機能を追加しました。
							エクスポートを動作させるためにMicrosoft Excelのインストールは一切不要。
							SyncVV-IIソフトウェアのみでテイクリストを扱いやすいExcel形式に変換できます。
							エクスポートしたExcel形式ファイルには、テイクに関連する情報だけでなく、映像サムネイルも同時にExcelシートに保存。
							収録素材の状態を他の端末でも一目瞭然に把握できます。
						</p>
					</div>
				</details>

				<details>
					<summary>Microsoft ExcelからGoogle Sheetsへ</summary>
					<div class="dynamic-image-text-flexbox">
						<p>
							<img alt="" src={image32} style="float:left" />
						</p>

						<p>
							沢山の時間を使って収録を行なう現場から、撮影素材がポストプロダクションへ渡った段階から、新たな挑戦が始まります。
							膨大な収録済みテイクの中から作業に必要な対象テイクを抜き出し、必要なデータに変換を行なう作業は、ミスの許されない作業。
							事前の入念な確認が欠かせないプロセスです。
							テイクリストのExcelファイルエクスポートを使ってExcel形式に変換した後、クラウドネイティブなGoogle
							Sheetsにアップロードしてチームに共有するのはいかがでしょうか？
							SyncVV-IIの開発チームによって、Microsoft ExcelからGoogle
							Sheetsへの変換プロセスについても事前に検証済み。
							サムネイル付きテイク情報をいつでもどこでも確認できる、新しいスタイルの撮影ワークフロー構築に貢献します。
						</p>
					</div>
				</details>

				<details>
					<summary>考え抜かれたディレクトリ構造によるデータ管理</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image33} style="float:left" /></p>

						<p>
							SyncVV-IIは、見えない部分もこだわり抜いて設計されています。
							データ管理を安全かつ効率的に行なうための、考え抜かれたディレクトリ構造もそのひとつ。
							ソフトウェアによるプロジェクト管理はもちろんのこと、手動によるデータバックアップや、異なる端末へのプロジェクトデータコピーまでを念頭に入れて設計されています。
							貴重な撮影データを1バイトも逃さないデータ管理を考え抜いたディレクトリ構造は、厳しい撮影現場の視点から生まれました。
						</p>
					</div>
				</details>

				<details>
					<summary>オートメーションを可能にするプロジェクトファイル形式</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image34} style="float:left" /></p>

						<p>
							SyncVV-IIのプロジェクトファイルは、JavaScript Object Notation
							(JSON)形式のテキストファイルとして保存されます。
							データの内容は全て公開されており、独自のアプリケーションを構築する事も可能。
							ワークフローの自動化に興味のある先進的なユーザーのニーズも捉えたユニークな配慮です。
							SyncVV-IIは、単体システムとしての活用のみならず、ワークフロー全体の効率的な活用にまで配慮しています。
						</p>
					</div>
				</details>

				<details>
					<summary>クラウド型ファイル共有サービスに対応</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image35} style="float:left" /></p>

						<p>
							クラウド型ファイル共有サービスを用いたプロジェクト同期に興味はありますか？
							SyncVV-IIでは、プロジェクトディレクトリを丸ごとクラウド型ファイル共有サービスの管理下に置くことで、冗長性の高いシステムを簡単に実現可能。
							システムによって異なるルートプロジェクトディレクトリでも、正しくプロジェクトを扱えるように数々の配慮がなされています。
							収録した瞬間からクラウドを経由して様々な端末にプロジェクトを共有する事で、収録素材の安全性確保にも貢献。
							新しい世代の収録システムは、クラウドを用いた先進的な統合環境を提供します。
						</p>
					</div>
				</details>
			</div>

			<div class="container">
				<h3>最新最強の収録再生システム</h3>
				<p class="explanation-big">SyncVV II は紛れなく最新最強の収録再生システムです。</p>

				<details>
					<summary>長年培ったリアルタイムシステム技術による高い安定性を確保</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image36} style="float:left" /></p>

						<p>
							リベラルロジック株式会社が長年培ったリアルタイムシステム技術は、SyncVV-IIの基幹設計と言える広帯域データフローの実現に貢献しています。
							システムプロセッサコアを最大限効率的に使用する並列化計算処理技術もそのひとつ。
							SDI入力処理、リアルタイム映像処理、リアルタイムエンコーディング処理、ユーザーインターフェース処理と、汎用オペレーティングシステムであるWindows上においてリアルタイムシステムを構成するには、熟練の技術が必要不可欠です。
							リベラルロジック株式会社のリアルタイムシステム技術は、SyncVV-IIの4系統並列稼働リアルタイムシステムの根幹を支えるものになっています。
						</p>
					</div>
				</details>

				<details>
					<summary>世界中のオペレータから集めたフィードバックを元に設計</summary>
					<div class="dynamic-image-text-flexbox">
						<p><img alt="" src={image37} style="float:left" /></p>

						<p>
							SyncVV-IIは、世界中のオペレータから集めたフィードバックを元に設計されました。
							数ある要求を元に、運用負荷を大幅に低減すること、頼れる収録再生ソフトウェアとすること、を念頭に設計。
							熟練の技術に加えて、常に新たな挑戦を加えて、日々進化し続けるソフトウェアの世界を構築しています。
							新しい世界は常に現場から。
							これまでも、これからも、SyncVVシリーズは顧客と共に新しい世界に向かって成長を続けます。
						</p>
					</div>
				</details>
			</div>
		</section>

		<section class="support" id="support">
			<div class="container">
				<h2>サポート</h2>
				<h3>SyncVV(2015)からの移行</h3>
				<h3>はじめに</h3>
				<ul>
					<li>
						「SyncVV(2015)からの移行」では、旧来のシステムを御利用の御客様がSyncVV-IIに移行を検討する際に役立つ情報が記載されています。スムースな移行のために事前に十分な時間的余裕の確保とバックアップを行なってから移行作業を開始することを強く推奨します。
					</li>
					<li>
						SyncVV(2015)システムは長期に渡って供給されている製品のため、導入時期によっては現在お使いのハードウェアがそのまま使用できない場合がございます。この場合、新しくハードウェアを御用意しての御提供となりますことを予め御了承下さい。
					</li>
					<li>
						SyncVV(2015)とSyncVV-IIは一部実現機能が異なります。御客様の要件にSyncVV-IIが適合しない場合、SyncVV(2015)の使用を継続する事を御検討下さい。
					</li>
				</ul>

				<h2>機能比較</h2>

				<h3>ハードウェア</h3>

				<table border="1" cellspacing="1">
					<thead>
						<tr>
							<th>項目</th>
							<th>SyncVV(2015)</th>
							<th>SyncVV-II</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>SDI I/O Card</td>
							<td>Bluefish Supernova S+ (x2)</td>
							<td>Bluefish Supernova S+ (x2)</td>
						</tr>
						<tr>
							<td>External LTC Input</td>
							<td>1</td>
							<td>1</td>
						</tr>
						<tr>
							<td>NVIDIA NVENC/NVDEC対応GPU</td>
							<td>不要</td>
							<td>必須 (A)</td>
						</tr>
						<tr>
							<td>RAID System</td>
							<td>必須</td>
							<td>推奨</td>
						</tr>
					</tbody>
				</table>

				<h3>ソフトウェア</h3>

				<table border="1" cellspacing="1">
					<thead>
						<tr>
							<th>項目</th>
							<th>SyncVV(2015)</th>
							<th>SyncVV-II</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>Windows 10対応 / Windows 11対応</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>リサイズ可能なアプリケーションウィンドウ</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>フルスクリーンアプリケーションモード</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>SDI収録機能</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>SDI再生機能</td>
							<td>対応</td>
							<td>- (B)</td>
						</tr>
						<tr>
							<td>Vicon連携動作機能</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Vicon連携動作方式</td>
							<td>外部コマンドプログラム</td>
							<td>統合プラグインシステム</td>
						</tr>
						<tr>
							<td>Vicon連携タイムコード先頭フレーム同期</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Vicon連携タイムコード最終フレーム同期</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Vicon連携テイク名受け渡し</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Vicon連携テイクノート受け渡し</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Vicon連携テイク詳細情報受け渡し</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>タイムコードのドロップフレーム表記対応</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>タイムコード焼き込み機能</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>タイムコード焼き込み位置指定機能</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>タイムコード焼き込みサイズ指定機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>タイムコード焼き込み前景色指定機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>タイムコード焼き込み背景色指定機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>QuickTime (MOVコンテナ) 形式</td>
							<td>対応 (C)</td>
							<td>-</td>
						</tr>
						<tr>
							<td>DNxHD (MOVコンテナ) 形式</td>
							<td>対応 (C)</td>
							<td>-</td>
						</tr>
						<tr>
							<td>H.264 (MP4コンテナ) 形式</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>H.265 (MP4コンテナ) 形式</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>プレビューの回転表示機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>ラージプレビュー機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>ラージプレビュー機能のレイアウト選択機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>ディレクター用ウィンドウプレビュー機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>プロジェクト管理機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>プロジェクト読み込み機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>プロジェクト書き込み機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>大きく見やすいテイクリスト</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクのレイティング機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクのカラー機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクのノート機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクの詳細説明機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクリストの表示高さ調整</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクリストの素材サムネイル機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクリストの素材サムネイル拡大縮小</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクリストの素材ダブルクリック再生</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクリストのMicrosoft Excelエクスポート</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクのフィルタリング表示機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクのエクスポート機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>プロジェクトフォルダを開く</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>テイクフォルダを開く</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>エンベデッドオーディオのモニタリング</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>エンベデッドオーディオのレベルメータ</td>
							<td>選択した1系統を表示</td>
							<td>全4系統を常に表示</td>
						</tr>
						<tr>
							<td>エンベデッドオーディオの波形モニタ</td>
							<td>-</td>
							<td>トレンドグラフ表示</td>
						</tr>
						<tr>
							<td>収録開始タイムコード記録機能</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>収録終了タイムコード記録機能</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>収録開始システム時刻記録機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>収録終了システム時刻記録機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>収録済み素材PC再生機能</td>
							<td>- (C)</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>収録時収録時間長表示機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>収録時の信号断絶</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>静止画像キャプチャ</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>コンポジットガイド機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>階層化された収録データ管理機能</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>GPUアクセラレーションエンコーダー</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>GPUアクセラレーションタイムコード焼き込み</td>
							<td>対応</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>ショートカットキーによる操作</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Dropboxを使ったプロジェクト共有</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Synologyを使ったプロジェクト共有</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Stream Deck Mini</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Stream Deck</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Stream Deck MK.2</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Stream Deck XL</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Stream Deck Pedal</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>Pythonプロジェクトファイルリーダー</td>
							<td>-</td>
							<td>対応</td>
						</tr>
						<tr>
							<td>ユーザーマニュアル</td>
							<td>-</td>
							<td>対応 (英語/日本語)</td>
						</tr>
						<tr>
							<td>リリースノート</td>
							<td>-</td>
							<td>対応 (英語/日本語)</td>
						</tr>
						<tr>
							<td>ユーザーインターフェース言語対応</td>
							<td>- (D)</td>
							<td>対応 (英語/日本語)</td>
						</tr>
					</tbody>
				</table>

				<ul>
					<li>
						<p>
							(A) NVIDIA Video Encode and Decode GPU Support Matrix (&nbsp;<a
								href="https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new"
								rel="noopener"
								target="_blank"
								>https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new</a
							>&nbsp;) を御参照頂き、同時インスタンス数4以上のモデルを御採用下さい。
						</p>
					</li>
					<li>
						<p>(B) 収録済み素材はWindows上の再生ソフトウェアを使って再生します。</p>
					</li>
					<li>
						<p>(C) アップル社はWindows版QuickTimeのサポート終了を発表しています。</p>
					</li>
					<li>
						<p>(D) SyncVV(2015)のユーザーインターフェースは英語のみサポートしています。</p>
					</li>
					<li>
						<p>
							Microsoft Excelは、米国Microsoft
							Corporationの米国およびその他の国における登録商標または商標です。
						</p>
					</li>
				</ul>
			</div>
		</section>

		<!-- <section class="contact" id="contact"></section> -->
	</div>
</div>

<style>
	td,
	tr {
		font-size: calc(14px + 0.390625vw);
	}
	.dynamic-iframe {
		float: left;
		height: 40vh;
	}
	li {
		font-size: calc(14px + 0.390625vw);
	}

	.overflowed-text {
		margin: 0;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 3;
		white-space: pre-wrap;
	}
	.sidebar-item {
		font-size: calc(14px + 0.390625vw);
		color: #ababab;
		padding: 16px;
		text-decoration: none;
	}
	.sidebar-item.active {
		color: #000000;
		font-size: calc(14px + 0.390625vw);
	}
	.features-list {
		padding-left: 5rem;
	}
	.features-list-item {
		list-style-type: disc;
		font-size: calc(14px + 0.390625vw);
		line-height: 1.5;
	}
	.pageContent {
		padding: 2rem 8rem;
	}
	.sidebar {
		margin: 0;
		padding: 0;
		width: 25vw;
		position: absolute;
		height: 100%;
		overflow: auto;
		display: flex;
		flex-direction: column;
	}

	.sidebar-fixed {
		position: fixed;
		top: 0;
		left: 0;
		padding: 2rem 0 2rem 8rem;
	}

	.content {
		margin-left: 25vw;
		padding: 1px 16px;
	}

	.relatedLinks {
		overflow: hidden;
		padding: 4rem 0;
		background-color: #dddddd;
		margin: 5rem 0 0 0;
		text-align: center;
		width: 100%;
	}
	.card article figure {
		margin: 0;
		width: inherit;
		-webkit-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		-moz-box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		box-shadow: 0px 2px 12px 2px rgba(173, 173, 173, 1);
		border-radius: 8px;
		height: 100%;
	}

	.card article figure figcaption {
		padding: 15px;
		display: flex;
		flex-direction: column;
		align-items: baseline;
		gap: 0.5rem;
		font-size: calc(11px + 0.390625vw);
		text-align: left;
		min-height: 8rem;
		background: white;
	}

	.card article figure a img {
		width: 100%;
		height: auto;
		border-radius: 8px 8px 0 0;
		cursor: pointer;
		display: block;
		max-height: 160px;
		object-fit: cover;
	}
	.cardList {
		width: 100%;
		margin-top: 3rem;
		display: flex;
		justify-content: center;
		align-items: flex-start;
		list-style: none;
	}

	.cardList .card {
		width: 15.5rem;
		margin-right: 2rem;

		&:last-child {
			margin-right: 0;
		}
	}

	.cardListMobile {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(auto-fill, 13.5rem);
		grid-gap: 2rem;
		justify-content: center;
		align-content: flex-start;
		list-style: none;
		margin: 2vh auto;
		padding: 0 0 1.5vh 0;
		overflow: hidden;
	}

	.cardListMobile .card {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.hero {
		position: relative;
		margin-bottom: 5rem;
	}

	.hero-image-container {
		max-height: 105vh;
		overflow: hidden;
		display: flex;
		justify-content: center;
		align-items: center;
		border-radius: 15px;
	}

	.hero-image {
		width: 100%;
		max-height: 100%;
		object-fit: contain;
	}

	p {
		margin: 0;
		font-size: calc(14px + 0.390625vw);
	}
	.explanation {
		font-size: calc(14px + 0.390625vw);
	}
	.explanation-big {
		font-size: calc(18px + 0.390625vw);
	}
	h1 {
		font-size: calc(36px + 0.390625vw);
		font-weight: 600;
		padding: 4rem 0;
	}
	h2 {
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}

	h3 {
		font-size: calc(28px + 0.390625vw);
		font-weight: 600;
		color: #0b345b;
	}

	section:not(.relatedLinks) {
		width: 100%;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 0;
		border-top: 2px solid black;
	}

	.container {
		display: flex;
		gap: 2rem;
		padding: 3rem 0;
		flex-direction: column;
	}
	/* section div div {
		display: flex;
		flex-direction: column;
		flex: 50%;
		justify-content: space-between;
	} */
	section div figure {
		flex: 50%;
	}
	section div figure img {
		width: 100%;
	}

	figure {
		margin: 0;
		padding: 0;
		text-align: left;
	}

	@media (max-width: 800px) {
		.container {
			flex-direction: column;
		}

		.cardList {
			grid-template-columns: repeat(auto-fill, 15.5rem);
			margin: 0 auto;
		}
	}

	@media screen and (max-width: 700px) {
		.dynamic-iframe {
			width: auto;
		}
		.sidebar {
			width: 100%;
			height: auto;
			position: relative;
			flex-direction: row;
			justify-content: flex-start;
			align-items: center;
		}
		.sidebar-fixed {
			background-color: white;
		}
		.hero {
			margin-bottom: 2rem;
		}
		.sidebar-fixed {
			position: fixed;
			padding: 0rem;
		}
		.sidebar a {
			float: left;
		}
		div.content {
			margin-left: 0;
		}
		iframe {
			width: 100%;
		}
	}

	@media screen and (max-width: 1200px) {
		.pageContent {
			padding: 0 1rem;
		}
		h1 {
			padding: 2rem 0;
		}
	}

	@media screen and (max-width: 400px) {
		.sidebar a {
			text-align: center;
			float: none;
		}
	}
</style>
