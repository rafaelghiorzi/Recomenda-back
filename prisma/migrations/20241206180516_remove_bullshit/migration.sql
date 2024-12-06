/*
  Warnings:

  - You are about to drop the column `imdbId` on the `Movie` table. All the data in the column will be lost.
  - You are about to drop the column `tmdbId` on the `Movie` table. All the data in the column will be lost.
  - Added the required column `timestamp` to the `Rating` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Movie" DROP COLUMN "imdbId",
DROP COLUMN "tmdbId";

-- AlterTable
ALTER TABLE "Rating" ADD COLUMN     "timestamp" INTEGER NOT NULL,
ALTER COLUMN "createdAt" SET DEFAULT CURRENT_TIMESTAMP;

-- AlterTable
ALTER TABLE "Tag" ALTER COLUMN "createdAt" SET DEFAULT CURRENT_TIMESTAMP;
