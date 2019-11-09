function sFiles = calculateDataCovariance(sFiles)

% Start a new report
bst_report('Start', sFiles);

% Process: Compute covariance (noise or data)
sFilesOut = bst_process('CallProcess', 'process_noisecov', sFiles, [], ...
    'baseline',       [], ...
    'datatimewindow', [], ...
    'sensortypes',    'MEG, EEG, SEEG, ECOG', ...
    'target',         1, ...  % Noise covariance     (covariance over baseline time window)
    'dcoffset',       2, ...  % Compute global average and remove it to from all the blocks
    'identity',       0, ...
    'copycond',       0, ...
    'copysubj',       0, ...
    'copymatch',      0, ...
    'replacefile',    1);  % Replace

% Process: Compute covariance (noise or data)
sFilesOut = bst_process('CallProcess', 'process_noisecov', sFiles, [], ...
    'baseline',       [], ...
    'datatimewindow', [], ...
    'sensortypes',    'MEG, EEG, SEEG, ECOG', ...
    'target',         2, ...  % Noise covariance     (covariance over baseline time window)
    'dcoffset',       2, ...  % Compute global average and remove it to from all the blocks
    'identity',       0, ...
    'copycond',       0, ...
    'copysubj',       0, ...
    'copymatch',      0, ...
    'replacefile',    1);  % Replace

% Save and display report
ReportFile = bst_report('Save', sFilesOut);
bst_report('Open', ReportFile);
% bst_report('Export', ReportFile, ExportDir);