const { User } = require("../models");

module.exports = {
    index: (req, res) => {
        return res.status(200).json({
            success: true,
            message: "Akhirnya bisa deploy.... 2",
        })
    },

    signup: (req, res) => {

        const {id, username, name, password, profile_picture, level} = req.body;
        const newUserObj = { id, username, name, password, profile_picture, level};
        const newUser = new User(newUserObj);

        newUser.save((saveErr) => {
            if(saveErr) {
                return res.status(412).send({
                    success: false,
                    message: saveErr
                })
            }
            return res.status(200).json({
                success: true,
                message: "signup successful"
            });
        });
        
        
    }

}
