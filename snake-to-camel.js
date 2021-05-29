function snakeToCamel(snakeCased) {    return snakeCased.replace(/(_\w)/g, function (match) {
    
    return match.toUpperCase().substr(1);
});
}

