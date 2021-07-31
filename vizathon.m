opts = delimitedTextImportOptions("NumVariables", 7);

% Specify range and delimiter
opts.DataLines = [2, Inf];
opts.Delimiter = ",";

% Specify column names and types
opts.VariableNames = ["year", "title", "binary", "budget", "domgross", "intgross", "totalgross"];
opts.VariableTypes = ["double", "string", "categorical", "double", "double", "double", "double"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Specify variable properties
opts = setvaropts(opts, "title", "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["title", "binary"], "EmptyFieldRule", "auto");

% Import the data
bechdel = readtable("C:\Users\aruni\OneDrive\Documents\testdata.csv", opts)
[totalGross, intGross, domGross, budget, binary, title, year] = readvars('C:\Users\aruni\OneDrive\Documents\testdata.csv');
whos  totlaGross intGross domGross budget binary title year
%print(bechdel.totalGross)
%plot(bechdel.X, bechdel.Y)
%x = bechdel(9, :);
%y = bechdel(:, 8);
%bar(x, y);

p=bechdel{:,1};
q=bechdel{:,2};
save('bechdel.mat','p','q')

load bechdel.mat
traindata
knnmodel = fitcknn(traindata,"Character","NumNeighbors",5,"Standardize",true,"DistanceWeight","squaredinverse");
testdata




