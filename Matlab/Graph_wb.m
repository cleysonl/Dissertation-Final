fis = readfis('Wb');
opt = gensurfOptions;
opt.InputIndex = [3 2];
opt.NumGridPoints = 20;
opt.ReferenceInputs = [.5 NaN NaN];
gensurf(fis,opt);


%%%%
ruleview('Wb')

