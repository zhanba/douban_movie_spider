
/*==============================================================*/
/* Table: movies                                                */
/*==============================================================*/
create table movies (
   uuid                 uuid                 not null,
   update_time          timestamp            null,
   subject_id           VARCHAR(50)          not null,
   name                 VARCHAR(1000)        not null,
   year                 INT                  null,
   cover_url            VARCHAR(1000)        null,
   directors            VARCHAR(1000)[]      null,
   writers              VARCHAR(1000)[]      null,
   actors               VARCHAR(1000)[]      null,
   genres               VARCHAR(1000)[]      null,
   site                 VARCHAR(1000)        null,
   countries            VARCHAR(1000)[]      null,
   languages            VARCHAR(200)[]       null,
   release_date         VARCHAR(1000)        null,
   season               INT                  null,
   episode              INT                  null,
   episode_time         INT                  null,
   running_time         INT                  null,
   alias                VARCHAR(1000)[]      null,
   imdb_link            VARCHAR(1000)        null,
   rating               real                 null,
   rating_num           int                  null,
   summary              TEXT                 null,
   tags                 VARCHAR(1000)[]      null,
   constraint PK_MOVIES primary key (uuid)
);

/*==============================================================*/
/* Index: movies_PK                                              */
/*==============================================================*/
create unique index movies_PK on movies (
uuid
);
