<script>
	import { onMount } from 'svelte';

	const modalOpenBtns = document.querySelectorAll('.modal-open');
	const modalCloseBtns = document.querySelectorAll('.modal-close');
	const body = document.querySelector('body');

	onMount(() => {
		modalOpenBtns.forEach((btn) => {
			btn.addEventListener('click', (e) => {
				let modal = btn.getAttribute('data-modal');
				document.getElementById(modal).style.display = 'block';
				body.classList.add('prevent-background-scroll');
			});
		});

		// modalCloseBtns.forEach((btn) => {
		// 	btn.addEventListener('click', (e) => {
		// 		let modal = (btn.closest('.modal').style.display = 'none');
		// 		body.classList.remove('prevent-background-scroll');
		// 	});
		// });
		// document.addEventListener('click', (e) => {
		// 	if (e.target.classList.contains('modal')) {
		// 		e.target.style.display = 'none';
		// 		body.classList.remove('prevent-background-scroll');
		// 	}
		// });
	});
</script>

<section id="content">
	<!-- Cards -->
	<div class="card">
		<img
			class="card-img"
			src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/8970757c-5e57-43ee-9014-60640eaa2469"
		/>
		<div class="title">
			<h2>Beer Galore</h2>
		</div>
		<div class="more">
			<button class="modal-open" data-modal="modal1">
				more<ion-icon class="open-icon" name="open-outline" aria-hidden="true" />
			</button>
		</div>
	</div>

	<div class="card">
		<img
			class="card-img"
			src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/98d23019-9931-4e20-a823-30724a018d9c"
		/>
		<div class="title">
			<h2>Bavarian Culture Showcase</h2>
		</div>
		<div class="more">
			<button class="modal-open" data-modal="modal2">
				more<ion-icon class="open-icon" name="open-outline" aria-hidden="true" />
			</button>
		</div>
	</div>

	<div class="card">
		<img
			class="card-img"
			src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/58bdbc26-b73b-4066-99ba-cbbfb45214d6"
		/>
		<div class="title">
			<h2>Souvenirs and Shopping</h2>
		</div>
		<div class="more">
			<button class="modal-open" data-modal="modal3">
				more<ion-icon class="open-icon" name="open-outline" aria-hidden="true" />
			</button>
		</div>
	</div>

	<div class="card">
		<img
			class="card-img"
			src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/be357710-c460-45e8-a61e-2db9c45eb12b"
		/>
		<div class="title">
			<h2>Bavarian Culinary Delights</h2>
		</div>
		<div class="more">
			<button class="modal-open" data-modal="modal4">
				more<ion-icon class="open-icon" name="open-outline" aria-hidden="true" />
			</button>
		</div>
	</div>

	<div class="card">
		<img
			class="card-img"
			src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/e2f37f05-f3a7-45b9-83dc-1e1ab9212e43"
		/>
		<div class="title">
			<h2>Live Music and Entertainment</h2>
		</div>
		<div class="more">
			<button class="modal-open" data-modal="modal5">
				more<ion-icon class="open-icon" name="open-outline" aria-hidden="true" />
			</button>
		</div>
	</div>

	<div class="card">
		<img
			class="card-img"
			src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/82bb545a-3d20-442c-9670-191105298b4b"
		/>
		<div class="title">
			<h2>Fun and Games</h2>
		</div>
		<div class="more">
			<button class="modal-open" data-modal="modal6">
				more<ion-icon class="open-icon" name="open-outline" aria-hidden="true" />
			</button>
		</div>
	</div>

	<!-- Modals -->
	<div class="modal" id="modal1">
		<div class="modal-content">
			<div class="modal-header">
				Beer Galore<button class="modal-close">
					<ion-icon class="close-icon" name="close-outline">Close</ion-icon>
				</button>
			</div>
			<div class="modal-body modal-one">
				<img
					src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/8970757c-5e57-43ee-9014-60640eaa2469"
					alt=""
				/>
				<ul>
					<li>
						Savor a wide variety of world-famous German beers, including lagers, ales, and stouts.
					</li>
					<li>
						Raise your stein high and enjoy traditional Bavarian toasts with friends old and new.
					</li>
					<li>Be sure to try the special brews crafted exclusively for Oktoberfest.</li>
				</ul>
			</div>
			<div class="modal-footer">
				<button class="button close-btn modal-close">Close</button>
			</div>
		</div>
	</div>

	<div class="modal" id="modal2">
		<div class="modal-content">
			<div class="modal-header">
				Bavarian Culture Showcase<button class="modal-close">
					<ion-icon class="close-icon" name="close-outline">Close</ion-icon>
				</button>
			</div>
			<div class="modal-body">
				<img
					src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/98d23019-9931-4e20-a823-30724a018d9c"
					alt=""
				/>
				<ul>
					<li>
						Immerse yourself in the rich Bavarian culture with art exhibitions and demonstrations.
					</li>
					<li>
						Learn about the history and traditions of Oktoberfest through informative displays.
					</li>
				</ul>
			</div>
			<div class="modal-footer">
				<button class="button close-btn modal-close">Close</button>
			</div>
		</div>
	</div>

	<div class="modal" id="modal3">
		<div class="modal-content">
			<div class="modal-header">
				Souvenirs and Shopping<button class="modal-close">
					<ion-icon class="close-icon" name="close-outline">Close</ion-icon>
				</button>
			</div>
			<div class="modal-body">
				<img
					src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/58bdbc26-b73b-4066-99ba-cbbfb45214d6"
					alt=""
				/>
				<ul>
					<li>Shop for unique Bavarian souvenirs, clothing, and trinkets at our market stalls.</li>
					<li>Take home a piece of Oktoberfest to remember this incredible experience.</li>
				</ul>
			</div>
			<div class="modal-footer">
				<button class="button close-btn modal-close">Close</button>
			</div>
		</div>
	</div>

	<div class="modal" id="modal4">
		<div class="modal-content">
			<div class="modal-header">
				Bavarian Culinary Delights<button class="modal-close">
					<ion-icon class="close-icon" name="close-outline">Close</ion-icon>
				</button>
			</div>
			<div class="modal-body">
				<img
					src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/be357710-c460-45e8-a61e-2db9c45eb12b"
					alt=""
				/>
				<ul>
					<li>
						Indulge in mouthwatering German cuisine, from bratwurst and schnitzel to pretzels and
						sauerkraut.
					</li>
					<li>
						Experience the rich flavors of authentic Bavarian dishes prepared by skilled chefs.
					</li>
				</ul>
			</div>
			<div class="modal-footer">
				<button class="button close-btn modal-close">Close</button>
			</div>
		</div>
	</div>

	<div class="modal" id="modal5">
		<div class="modal-content">
			<div class="modal-header">
				Live Music and Entertainment<button class="modal-close">
					<ion-icon class="close-icon" name="close-outline">Close</ion-icon>
				</button>
			</div>
			<div class="modal-body">
				<img
					src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/e2f37f05-f3a7-45b9-83dc-1e1ab9212e43"
					alt=""
				/>
				<ul>
					<li>Get your groove on with live traditional German bands and folk dancers.</li>
					<li>
						Expect a vibrant atmosphere filled with music, dancing, and cultural performances.
					</li>
				</ul>
			</div>
			<div class="modal-footer">
				<button class="button close-btn modal-close">Close</button>
			</div>
		</div>
	</div>

	<div class="modal" id="modal6">
		<div class="modal-content">
			<div class="modal-header">
				Fun and Games<button class="modal-close">
					<ion-icon class="close-icon" name="close-outline">Close</ion-icon>
				</button>
			</div>
			<div class="modal-body">
				<img
					src="https://github.com/ecemgo/mini-samples-great-tricks/assets/13468728/82bb545a-3d20-442c-9670-191105298b4b"
					alt=""
				/>
				<ul>
					<li>
						Participate in traditional Oktoberfest games, including stein-holding contests and
						bratwurst-eating competitions.
					</li>
					<li>
						Bring the whole family; we have activities for all ages, including a dedicated kids'
						zone.
					</li>
				</ul>
			</div>
			<div class="modal-footer">
				<button class="button close-btn modal-close">Close</button>
			</div>
		</div>
	</div>
</section>

<style>
	.button:after,
	.close-btn:after {
		background: #fff;
	}

	.close-btn,
	.close-btn:before {
		background: rgba(255, 193, 7, 1);
		background: linear-gradient(45deg, rgba(255, 193, 7, 1) 0%, rgba(255, 87, 34, 1) 100%);
		background: -moz-linear-gradient(45deg, rgba(255, 193, 7, 1) 0%, rgba(255, 87, 34, 1) 100%);
		background: -webkit-linear-gradient(45deg, rgba(255, 193, 7, 1) 0%, rgba(255, 87, 34, 1) 100%);
	}

	.button {
		display: inline-block;
		position: relative;
		border-radius: 10px;
		text-decoration: none;
		padding: 1rem 2rem;
		font-size: 1rem;
		font-weight: bold;
		border: none;
		outline: none;
		cursor: pointer;
		transition: all 0.5s ease;
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.button:hover {
		text-shadow: 0px 0px 0px rgba(255, 255, 255, 0.8);
	}

	.button:hover::after {
		left: 100%;
		top: 100%;
		bottom: 100%;
		right: 100%;
	}

	.button::before {
		content: '';
		display: block;
		position: absolute;
		left: 0;
		top: 0;
		bottom: 0;
		right: 0;
		z-index: -1;
		border-radius: inherit;
		transition: all 0.5s;
	}

	.button::after {
		content: '';
		display: block;
		position: absolute;
		left: 2.5px;
		top: 2px;
		bottom: 2.5px;
		right: 2px;
		z-index: -1;
		border-radius: 8px;
		transition: all 0.5s;
	}

	/* -------- */
	/* CONTENT */

	#content {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 50px;
		padding: 60px 40px;
		min-height: 100dvh;
		overflow: hidden;
	}

	.card {
		position: relative;
		display: grid;
		grid-template-columns: 1fr;
		grid-template-rows: 50% 50%;
		border: 1px solid #000;
		width: 300px;
		aspect-ratio: 1/1;
		color: #fff;
		border-radius: 20px;
		box-shadow: 0 6.7px 5.3px rgba(0, 0, 0, 0.03), 0 22.3px 17.9px rgba(0, 0, 0, 0.05);
	}

	.title {
		display: flex;
		justify-content: center;
		align-items: center;
		color: #fff;
		background: #000;
		border-radius: 20px 20px 0 0;
		text-align: center;
	}

	.more {
		display: grid;
		grid-template-columns: 1fr 1fr;
		place-items: center;
		background-color: #fff;
		border-radius: 0 0 20px 20px;
	}

	.open-icon {
		font-size: 1.25rem;
		color: #000;
		transform: translateY(3px);
		margin-left: 3px;
		z-index: 1;
	}

	.modal-open {
		text-transform: uppercase;
		color: #000;
		background-color: transparent;
		outline: none;
		border: none;
		cursor: pointer;
		grid-area: 1 / 2 / span 1 / span 1;
	}

	.card-img {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		border-radius: 20px;
		object-fit: cover;
		object-position: 50% 50%;
		z-index: 2;
	}

	.card:hover > .card-img {
		animation: hovereffect 0.6s ease 1 normal forwards;
	}

	@keyframes hovereffect {
		0% {
			width: 100%;
			height: 100%;
			top: 0;
			border-radius: 20px;
		}

		100% {
			width: 50%;
			height: 50%;
			top: 50%;
			border-radius: 0 0 0 20px;
		}
	}

	/* ------ */
	/* MODAL */

	.modal {
		display: none;
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: rgba(0, 0, 0, 0.5);
		z-index: 20;
		animation: openModal 0.5s ease 1 normal;
	}

	@keyframes openModal {
		from {
			opacity: 0;
		}

		to {
			opacity: 1;
		}
	}

	.modal-content {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background: #fff;
		width: 50%;
		border-radius: 4px;
		z-index: 30;
	}

	.modal-header {
		position: relative;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		font-weight: 600;
		padding: 15px 20px 10px;
		font-size: 1.2rem;
	}

	.modal-header::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 1px;
		background: #d1d5db;
	}

	.modal-header .modal-close {
		background: #efefef;
		border: 0;
		outline: 0;
		transform: translateY(3px);
		background-color: transparent;
		cursor: pointer;
	}

	.close-icon {
		font-size: 1.6rem;
		color: #000;
	}

	.modal-body {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 30px 50px 10px;
		height: 70vh;
		overflow-y: auto;
	}

	.modal-one {
		padding: 70px 50px 10px;
	}

	.modal-body > img {
		max-width: 100%;
		width: 300px;
		aspect-ratio: 1/1;
		object-fit: cover;
		border-radius: 15px;
		margin-bottom: 20px;
	}

	.modal-footer {
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 10px 0 20px;
	}

	/* ------ */
	/* MEDIA QUERIES */

	@media (max-width: 1100px) {
		#content {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 800px) {
		#content {
			gap: 30px;
			padding: 60px 20px;
		}

		.card {
			width: 250px;
		}

		.modal-content {
			width: 80%;
		}
	}

	@media (max-width: 550px) {
		#content {
			grid-template-columns: repeat(1, 1fr);
			padding: 40px 40px;
		}
	}
</style>
