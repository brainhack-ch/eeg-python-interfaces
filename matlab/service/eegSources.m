function sFiles = eegAtlasSources(sFiles, atlas_name)
% Script generated by Brainstorm (15-Jan-2019)

% Start a new report
bst_report('Start', sFiles);

% Process: Compute sources [2018]
sFiles = bst_process('CallProcess', 'process_inverse_2018', sFiles, [], ...
    'output',  1, ...  % Kernel only: shared
    'inverse', struct(...
         'NoiseCovMat',    [], ...
         'DataCovMat',     [], ...
         'ChannelTypes',   {{}}, ...
         'InverseMethod',  'minnorm', ...
         'InverseMeasure', 'amplitude', ...
         'SourceOrient',   {{'fixed'}}, ...
         'Loose',          0.2, ...
         'UseDepth',       1, ...
         'WeightExp',      0.5, ...
         'WeightLimit',    10, ...
         'NoiseMethod',    'reg', ...
         'NoiseReg',       0.1, ...
         'SnrMethod',      'fixed', ...
         'SnrRms',         1000, ...
         'SnrFixed',       3, ...
         'FunctionName',   []));

% Process: Downsample to atlas
sFiles = bst_process('CallProcess', 'process_source_atlas', sFiles, [], ...
    'atlas',  atlas_name, ...
    'isnorm', 0);

% Save and display report
ReportFile = bst_report('Save', sFiles);
bst_report('Open', ReportFile);
% bst_report('Export', ReportFile, ExportDir);