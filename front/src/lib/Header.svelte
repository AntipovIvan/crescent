<script>
	import logo from '../assets/logo.png';
</script>

<header>
	<figure>
		<img src={logo} class="logo" alt="Crescent" width="170" height="80" />
	</figure>
	<nav>
		<label>
			<input type="checkbox" />
			<span class="menu"> <span class="hamburger" /> </span>
			<ul>
				<li><a href="#">製品販売</a></li>
				<li><a href="#">スタジオサービス</a></li>
				<li><a href="#">コンテンツ開発</a></li>
				<li><a href="#">会社情報</a></li>
				<li><a href="#">お問い合わせ</a></li>
			</ul>
		</label>
	</nav>
</header>

<style>
	a {
		text-decoration: none;
	}

	nav label a:link,
	nav label a:visited {
		background-color: white;
		color: black;
		text-align: center;
		display: inline-block;
	}

	nav label a:hover,
	nav label a:active {
		background-color: rgb(216, 216, 216);
	}

	header {
		background-color: #ffffff;
		color: #000000;
		padding: 0 40px;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
	}
	ul {
		list-style-type: none;
	}

	/* HEADER */
	.logo {
		width: 100%;
		max-width: 170px;
		height: auto;
	}

	nav label input {
		display: none;
	}

	nav label ul {
		display: flex;
		gap: 2rem;
		font-size: calc(12px + 0.390625vw);
	}

	@media only screen and (max-width: 600px) {
		/* HAMBURGER AND NAV */
		label .menu {
			position: absolute;
			right: -100px;
			top: -100px;
			z-index: 3;
			width: 200px;
			height: 200px;
			background: #fff;
			border-radius: 50% 50% 50% 50%;
			-webkit-transition: 0.5s ease-in-out;
			transition: 0.5s ease-in-out;
			box-shadow: 0 0 0 0 #fff, 0 0 0 0 #fff;
			cursor: pointer;
		}

		nav label .hamburger {
			position: absolute;
			top: 135px;
			left: 50px;
			width: 30px;
			height: 2px;
			background: #69d2e7;
			display: block;
			-webkit-transform-origin: center;
			transform-origin: center;
			-webkit-transition: 0.5s ease-in-out;
			transition: 0.5s ease-in-out;
		}

		nav label .hamburger:after,
		nav label .hamburger:before {
			-webkit-transition: 0.5s ease-in-out;
			transition: 0.5s ease-in-out;
			content: '';
			position: absolute;
			display: block;
			width: 100%;
			height: 100%;
			background: #69d2e7;
		}

		nav label .hamburger:before {
			top: -10px;
		}

		nav label .hamburger:after {
			bottom: -10px;
		}

		nav label input:checked + .menu {
			box-shadow: 0 0 0 100vw #fff, 0 0 0 100vh #fff;
			border-radius: 0;
		}

		nav label input:checked + .menu .hamburger {
			-webkit-transform: rotate(45deg);
			transform: rotate(45deg);
		}

		nav label input:checked + .menu .hamburger:after {
			-webkit-transform: rotate(90deg);
			transform: rotate(90deg);
			bottom: 0;
		}

		nav label input:checked + .menu .hamburger:before {
			-webkit-transform: rotate(90deg);
			transform: rotate(90deg);
			top: 0;
		}

		nav label input:checked + .menu + ul {
			opacity: 1;
		}

		nav label ul {
			z-index: 5;
			position: absolute;
			top: 50%;
			left: 50%;
			-webkit-transform: translate(-50%, -50%);
			transform: translate(-50%, -50%);
			opacity: 0;
			-webkit-transition: 0.25s 0s ease-in-out;
			transition: 0.25s 0s ease-in-out;
			display: block;
			gap: 2rem;
			font-size: 24px;
			width: max-content;
		}
		nav label a {
			margin-bottom: 1em;
			display: block;
			color: #f38630;
		}
	}
</style>
