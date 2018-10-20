const Promise = require('bluebird');

function request(param) {
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			console.log(param);
			if (param === 50 || param === 10) return reject(new Error('new Error'));
			resolve();
		}, 1000);
	});
}


async function p1() {
	let ops = [];
	const res = [];
	for(let i=0; i < 100; i++) {
		ops.push(request(i));
		if (i % concurencyLimit === 0) {
			res.concat(await Promise.all(ops));
			ops = [];
		}
	}
	if (ops.length > 0) res.concat(await Promise.all(ops));
	return res;
}

async function p2() {
	const locations = [];
	for(let i=0; i < 100; i++) {
		locations.push(i);
	}
	return await Promise.map(locations, (param) => {
		return request(param);
	}, { concurrency: 10 });
}

// p1()
p2()
	.then((results) => {
		console.log('finished', results);
	})
	.catch((err) => {
		console.log(err);
	});