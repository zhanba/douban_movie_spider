
/*==============================================================*/
/* Table: movie                                                 */
/*==============================================================*/
create table movie (
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
   countries            VARCHAR(1000)[]      null,
   languages            VARCHAR(200)[]       null,
   release_date         VARCHAR(1000)        null,
   running_time         INT                  null,
   alias                VARCHAR(1000)[]      null,
   imdb_link            VARCHAR(1000)        null,
   rating               real                 null,
   rating_num           int                  null,
   summary              TEXT                 null,
   tags                 VARCHAR(1000)[]      null,
   constraint PK_MOVIE primary key (uuid)
);

/*==============================================================*/
/* Index: movie_PK                                              */
/*==============================================================*/
create unique index movie_PK on movie (
uuid
);
