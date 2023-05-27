export interface Product {
	id: number;
	name: string;
	price: number;
	description: string;
	rating: number;
	url: string;
	image: string;
}

export const products_laptop = [
	{
		id: 1,
		name: 'Ноутбук Acer Nitro 5 AN515-57 NH.QEKER.004 черный',
		price: 389980,
		description: 'Acer Nitro 5',
		rating: 5,
		url: "https://kaspi.kz/shop/p/acer-nitro-5-an515-57-nh-qeker-004-chernyi-108194028/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h2e/hc4/67236399185950/acer-nitro-5-an515-57-nh-qeker-004-chernyi-108194028-1.jpg"
	},
	{
		id: 2,
		name: 'Ноутбук ASUS X515EA-BQ3144W I385SUW1 90NB0TY1-M02ZL0 темно-серый',
		price: 246990,
		description: 'ASUS X515EA-BQ3144W',
		rating: 7,
		url: "https://kaspi.kz/shop/p/asus-x515ea-bq3144w-i385suw1-90nb0ty1-m02zl0-temno-seryi-107650928/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb8/hbd/65953424277534/asus-x515ea-bq3144w-i385suw1-90nb0ty1-m02zl0-temno-seryi-107650928-1.jpg"
	},
	{
		id: 3,
		name: 'Ноутбук Lenovo IdeaPad 1 14IGL05 81VU00H3RU серый',
		price: 139990,
		description: 'Lenovo IdeaPad 1 14IGL05',
		rating: 9,
		url: "https://kaspi.kz/shop/p/lenovo-ideapad-1-14igl05-81vu00h3ru-seryi-108464874/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h5e/he2/67940461740062/lenovo-ideapad-1-14igl05-81vu00h3ru-seryi-108464874-1.jpg"
	},
	{
		id: 4,
		name: 'Ноутбук Lenovo IdeaPad 3 15ITL6 82H8005GRK серебристый',
		price: 169990,
		description: 'Lenovo IdeaPad 3 15ITL6',
		rating: 10,
		url: "https://kaspi.kz/shop/p/lenovo-ideapad-3-15itl6-82h8005grk-serebristyi-108090705/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h8f/h3a/66993674190878/lenovo-ideapad-3-15itl6-82h8005grk-serebristyi-108090705-1.jpg"
	},
	{
		id: 5,
		name: 'Ноутбук Apple MacBook Air 13 MGN63 серый',
		price: 478888,
		description: "Apple MacBook Air 13",
		rating: 3,
		url: "https://kaspi.kz/shop/p/apple-macbook-air-13-mgn63-seryi-100797845/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h65/h0f/33125684084766/apple-macbook-air-2020-13-3-mgn63-seryj-100797845-1-Container.jpg"
	}
];

export const products_phones = [
	{
		id: 1,
		name: 'Смартфон Apple iPhone 14 Pro Max 256Gb фиолетовый',
		price: 690270,
		description: 'Apple iPhone 14 Pro Max 256Gb',
		rating: 8,
		url: "https://kaspi.kz/shop/p/apple-iphone-14-pro-max-256gb-fioletovyi-106363342/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h00/h18/62948780834846/apple-iphone-14-pro-max-128gb-fioletovyj-106363342-1.jpg"
	},
	{
		id: 2,
		name: 'Смартфон Xiaomi Redmi 10C 4 ГБ/128 ГБ серый',
		price: 69275,
		description: 'Xiaomi Redmi 10C',
		rating: 4,
		url: "https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-128-gb-seryi-104417231/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hbc/h0a/49939925205022/xiaomi-redmi-10c-4-gb-128-gb-seryj-104417231-1.jpg"
	},
	{
		id: 3,
		name: 'Смартфон Xiaomi Redmi Note 10 Pro 8 ГБ/256 ГБ серый',
		price: 128350,
		description: 'Xiaomi Redmi Note 10 Pro',
		rating: 5,
		url: "https://kaspi.kz/shop/p/xiaomi-redmi-note-10-pro-8-gb-256-gb-seryi-107221005/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h45/h27/64487158087710/xiaomi-redmi-note-10-pro-8-gb-128-gb-seryi-107221005-1.jpg"
	},
	{
		id: 4,
		name: 'Смартфон Apple iPhone 11 128Gb Slim Box черный',
		price: 294000,
		description: 'Apple iPhone 11 128Gb',
		rating: 7,
		url: "https://kaspi.kz/shop/p/apple-iphone-11-128gb-slim-box-chernyi-100692388/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h17/h14/31489167425566/apple-iphone-11-128gb-slim-box-cernyj-100692388-1-Container.jpg"
	},
	{
		id: 5,
		name: 'Смартфон Samsung Galaxy A13 4 ГБ/128 ГБ черный',
		price: 88680,
		description: 'Samsung Galaxy A13',
		rating: 5,
		url: "https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-128-gb-chernyi-104253279/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h90/h49/49613711966238/samsung-galaxy-a13-4-gb-128-gb-chernyi-104253279-1.jpg"
	},
	
];

export const products_cameras = [
	{
		id: 1,
		name: 'Фотокамера моментальной печати Fujifilm Instax Mini 40 черный',
		price: 62899,
		description: 'Fujifilm Instax Mini 40',
		rating: 4,
		url: "https://kaspi.kz/shop/p/fujifilm-instax-mini-40-chernyi-102714918/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h2a/h84/46832941858846/fujifilm-instax-mini-40-cernyj-102714918-1.jpg"
	},
	{
		id: 2,
		name: 'Фотокамера Canon EOS 250D EF-S 18-55 IS STM Kit',
		price: 287930,
		description: ' Canon EOS 250D',
		rating: 7,
		url: "https://kaspi.kz/shop/p/canon-eos-250d-ef-s-18-55-is-stm-kit-2240118/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb2/h4b/32210465325086/canon-eos-250d-ef-s-18-55-is-stm-kit-black-2240118-1-Container.jpg"
	},
	{
		id: 3,
		name: 'Фотокамера моментальной печати Instax MINI 11 черный + пленка 10 шт',
		price: 56000,
		description: 'Instax MINI 11',
		rating: 3,
		url: "https://kaspi.kz/shop/p/instax-mini-11-chernyi-plenka-10-sht-103579208/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h22/hff/48551257767966/instax-mini-11-cernyj-plenka-10-st-103579208-1.jpg"
	},
	{
		id: 4,
		name: 'Фотокамера Sony Alpha ILCE7M4KB',
		price: 1399910,
		description: 'Sony Alpha series',
		rating: 10,
		url: "https://kaspi.kz/shop/p/sony-alpha-ilce7m4kb-103728127/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/haf/hd9/48803882926110/sony-alpha-ilce7m4kb-103728127-1.jpg"
	},
	{
		id: 5,
		name: 'Фотокамера Sony A7 IV Body',
		price: 1273985,
		description: 'Sony A7 IV',
		rating: 10,
		url: "https://kaspi.kz/shop/p/sony-a7-iv-body-103491027/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hde/h7e/48373562441758/sony-a7-iv-body-103491027-1.jpg"
	},
];

export const products_pcs = [
	{
		id: 1,
		name: 'Системный блок Impacto GLACIER PC белый',
		price: 366405,
		description: 'GLACIER PC',
		rating: 5,
		url: "https://kaspi.kz/shop/p/impacto-glacier-pc-belyi-104191528/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hd5/h73/49488952688670/impacto-glacier-pc-belyj-104191528-1.jpg"
	},
	{
		id: 2,
		name: 'Системный блок Andromeda PRO Life серый',
		price: 680000,
		description: 'Andromeda PRO Life',
		rating: 7,
		url: "https://kaspi.kz/shop/p/andromeda-pro-life-seryi-103586423/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc6/h10/66149327601694/andromeda-pro-life-seryi-103586423-1.jpg"
	},
	{
		id: 3,
		name: 'Системный блок GoodGame Start Gaming Pro 105 черный',
		price: 243284,
		description: 'GoodGame Start Gaming Pro',
		rating: 4,
		url: "https://kaspi.kz/shop/p/goodgame-start-gaming-pro-105-chernyi-108353707/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc4/h6f/67667853213726/goodgame-start-gaming-pro-105-chernyi-108353707-1.jpg"
	},
	{
		id: 4,
		name: 'Системный блок Cassian Thunder черный',
		price: 274944,
		description: 'Cassian Thunder',
		rating: 4,
		url: "https://kaspi.kz/shop/p/cassian-thunder-chernyi-108734960/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hee/h85/68589088374814/cassian-thunder-chernyi-108734960-1.jpg"
	},
	{
		id: 5,
		name: 'Системный блок Wintek Arrow черный',
		price: 201053,
		description: 'Wintek Arrow',
		rating: 3,
		url: "https://kaspi.kz/shop/p/wintek-arrow-chernyi-100723795/?c=750000000#!/item",
		image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h02/h6e/47959826464798/wintek-arrow-cernyj-100723795-1-Container.jpg"
	},

];


