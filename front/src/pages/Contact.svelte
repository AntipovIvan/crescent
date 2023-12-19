<script>
	import { onMount } from 'svelte';

	let products;
	let services;

	onMount(async () => {
		window.scrollTo(0, 0);
		const response1 = await fetch('http://' + window.location.hostname + ':7000/api/product');
		const data1 = await response1.json();

		const response2 = await fetch(
			'http://' + window.location.hostname + ':7000/api/servicesmodels'
		);
		const data2 = await response2.json();

		products = data1.results.sort(
			(a, b) => parseFloat(a.sorting_order) - parseFloat(b.sorting_order)
		);
		services = data2.results;
	});
</script>

<section class="section">
	<h1>お問い合わせ</h1>

	<div class="content">
		<p class="topParagraph">
			クレッセントへのお問い合わせは下記の連絡先、もしくは下部フォームよりお願い致します。
			なお、お問い合わせの前に必ず下部にあります注意事項をお読みください。
		</p>
		<h2>注意事項</h2>
		<ul>
			<li>
				土日、祝祭日、年末年始、夏期休暇期間等につきましては、翌営業日以降の対応となりますのでご了承ください
			</li>
			<li>
				メールアドレス、電話番号の記入に誤りがありますと、当社よりご連絡ができない場合がございますので、ご注意ください。
			</li>
			<li>
				万が一、当社からのご案内が無い場合は、お手数ですが弊社（03-5875-9707）までお電話にてお問い合わせください。
			</li>
		</ul>
	</div>

	<div class="content">
		<h2>連絡先</h2>
		<table>
			<tr>
				<td>TEL</td>
				<td>03-5875-9707（受付時間：祝日を除く月曜日～金曜日 10:00～17:30）</td>
			</tr>
			<tr>
				<td>FAX</td>
				<td>03-5875-9708</td>
			</tr>
			<tr>
				<td>E-mail</td>
				<td>info@crescentinc.co.jp</td>
			</tr>
		</table>
	</div>

	<div class="content">
		<h2>お問合せ用メールフォーム</h2>
		<form action="https://api.web3forms.com/submit" method="POST">
			<input type="hidden" name="access_key" value="8594de2d-073f-4531-8752-ca8a4efebdb4" />

			<label for="fname">お名前</label>
			<input type="text" id="fname" name="name" placeholder="例：山田　太郎..." required />

			<label for="furigana">フリガナ</label>
			<input type="text" id="furigana" name="name" placeholder="例：ヤマダ　タロウ..." required />

			<label for="orgname">企業名、学校名</label>
			<input type="text" id="orgname" name="title" placeholder="例：株式会社○○..." />

			<label for="services">製品名、サビス名</label>
			<select name="services" id="services">
				{#if products}
					{#each products as { id, title }, index}
						<option value={title}>{title}</option>
					{/each}
				{/if}

				{#if services}
					{#each services as { id, title }, index}
						<option value={title}>{title}</option>
					{/each}
				{/if}
			</select>

			<label for="address">住所</label>
			<input type="text" id="address" name="address" placeholder="例：東京都江東区3-2-12..." />

			<label for="phone">電話番号</label>
			<input type="tel" id="phone" name="phone" placeholder="例：03-5638-1819..." required />

			<label for="fax">FAX</label>
			<input type="tel" id="fax" name="fax" placeholder="例：03-5638-1818..." />

			<label for="mail">メールアドレス</label>
			<input type="email" id="mail" name="email" placeholder="info@crescentinc.co.jp..." required />

			<label for="message">コメント</label>
			<textarea id="message" name="message" required></textarea>

			<input type="hidden" name="redirect" value="https://web3forms.com/success" />
			<button type="submit">送信</button>
		</form>
	</div>
</section>

<style>
	input[type='text'],
	select,
	textarea,
	input[type='email'],
	input[type='tel'] {
		width: 100%;
		padding: 12px;
		border: 1px solid #ccc;
		border-radius: 4px;
		box-sizing: border-box;
		margin-top: 6px;
		margin-bottom: 16px;
		resize: vertical;
	}

	button[type='submit'] {
		background-color: #04aa6d;
		color: white;
		padding: 12px 20px;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	button[type='submit']:hover {
		background-color: #45a049;
	}

	table {
		font-family: arial, sans-serif;
		border-collapse: collapse;
		width: 100%;
	}

	td {
		border: none;
		text-align: left;
		padding: 8px;
		font-size: calc(14px + 0.390625vw);
	}
	.topParagraph {
		margin-bottom: 3rem;
	}
	.section {
		position: relative;
	}

	h1 {
		margin: 0 0 3rem 0;
		font-size: calc(32px + 0.390625vw);
		font-weight: 600;
	}
	h2 {
		padding-bottom: 1rem;
		width: max-content;
		color: #0b345b;
		font-size: calc(24px + 0.390625vw);
		font-weight: bold;
	}
	section {
		padding: 5rem;
		background-color: #efefef;
	}

	.content {
		display: flex;
		gap: 2rem;
		flex-wrap: wrap;
		flex-direction: column;
		margin-top: 2rem;
		margin-bottom: 5rem;
		align-items: baseline;
		padding-bottom: 8rem;
		margin: 0 20% 5rem 20%;
		border-bottom: 2px solid #101010;
	}

	.content ul {
		padding-left: 1.5rem;
	}
	.content ul li {
		list-style-type: disc;
		font-size: calc(16px + 0.390625vw);
	}

	p {
		margin: 0;
		font-size: calc(16px + 0.390625vw);
	}

	ul {
		margin: 0;
		padding: 0;
		list-style: none;
	}

	@media screen and (max-width: 950px) {
		.content {
			display: flex;
			gap: 2rem;
			flex-wrap: wrap;
			flex-direction: column;
			margin-top: 2rem;
			margin-bottom: 5rem;
			align-items: baseline;
			padding-bottom: 4rem;
			margin: 0 5% 2rem 5%;
			border-bottom: 2px solid #101010;
		}
		.section {
			padding: 1rem;
		}
	}
</style>
