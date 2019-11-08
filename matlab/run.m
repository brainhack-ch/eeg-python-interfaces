% path = 'D:\projects\brainstorm_db\eegfmri_london\data';
brainstorm

subjectNames = {'test'};
RawFilesMRI = {'D:\projects\geneva_256\T1\controls\sub-01'};

% import_fressurfer(subjectNames, RawFilesMRI);
bem_model(subjectNames);

%import data
importEEG_raw(subjectNames, RawFilesEEG);

%load generic EEG coordinates from template
setChannelFile(subjectNames, 'TODO template');

%filter data
%manual artifact reject

%import trails/segements

%manual coregistration or load coregistration

openmeeg_headmodel(subjectNames);
calculateDataCovariance(subjectNames);
calculateSources(subjectNames);
calculateConnectivity(subjectNames);