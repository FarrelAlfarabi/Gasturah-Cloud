import express from 'express';
import baseController from "../controllers/base-controller";
import validationMiddleware from '../middleware/validation-middleware';
const router = express();



router.get("/", baseController.index);
// router.post("/signup", validationMiddleware.signup, baseController.signup);
router.post("/signup", baseController.signup);


router.get("/signup", baseController.index);

module.exports = router;
