select sum(bytes)/1024/1024 size_in_mb from dba_data_files;

select sum(bytes)/1024/1024 size_in_mb from dba_segments;

select owner, sum(bytes)/1024/1024 Size_MB from dba_segments
group  by owner;