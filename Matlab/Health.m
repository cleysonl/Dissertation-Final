fis = readfis('Health');
opt = gensurfOptions;
opt.InputIndex = [1 3];
opt.NumGridPoints = 20;
opt.ReferenceInputs = [NaN 0.5 NaN];
gensurf(fis,opt)


%%%%
ruleview(fis)